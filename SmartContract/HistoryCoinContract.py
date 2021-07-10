import json
from web3 import Web3


class HistoryCoinContract:
    def __init__(self):
        self.w3 = Web3(Web3.HTTPProvider("HTTP://127.0.0.1:7545"))
        self.w3.eth.defaultAccount = self.w3.eth.accounts[0]
        self.connect_to_deployed_contract()

    def connect_to_deployed_contract(self):
        with open("SmartContract/CompilingAndDeploying/HistoryCoinAbiBin.json") as contract_json:
            data = json.load(contract_json)
            abi = data["contracts"]["../HistoryCoin.sol:HistoryCoin"]["abi"]
            with open("SmartContract/CompilingAndDeploying/HistoryCoinContractAddress", "r") as contract_address_file:
                address = contract_address_file.readline()
                self.contract = self.w3.eth.contract(address=address, abi=abi)

    def redeploy(self):
        from SmartContract.CompilingAndDeploying.deploy import deploy
        deploy()
        self.connect_to_deployed_contract()

    def get_message(self):
        return self.contract.functions.GetMessage().call()

    def set_message(self, message: str):
        tx_hash = self.contract.functions.SetMessage(message).transact()
        tx_receipt = self.w3.eth.wait_for_transaction_receipt(tx_hash)

    def make_proposal(self, text: str, lifetime_in_blocks: int):
        tx_hash = self.contract.functions.MakeProposal(text, lifetime_in_blocks).transact()
        return self.w3.eth.wait_for_transaction_receipt(tx_hash)

    # def get_totalSupply(self):
    #     return self.contract.functions

    def create_record(self, record_text, lifetime_in_blocks):
        return self.contract.functions.CreateRecord(record_text, lifetime_in_blocks).transact()

    def hello_world(self):
        return "hello world"

    def num_records(self):
        return self.contract.functions.GetNumberOfRecords().call()
