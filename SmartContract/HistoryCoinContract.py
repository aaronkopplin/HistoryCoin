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
        self.w3.eth.wait_for_transaction_receipt(tx_hash)

    def create_record(self, record_text, lifetime_in_blocks):
        tx_hash = self.contract.functions.CreateRecord(record_text, lifetime_in_blocks).transact()
        self.w3.eth.wait_for_transaction_receipt(tx_hash)

    def get_record_text(self, id: int):
        return self.contract.functions.GetRecordText(id).call()

    def get_total_supply(self):
        return self.contract.functions.GetTotalSupply().call()

    def get_balance_of_sender(self):
        return self.get_balance_of(self.w3.eth.defaultAccount)

    def get_balance_of(self, address):
        return self.contract.functions.balanceOf(address).call()

    def request_tokens(self, amount):
        tx_hash = self.contract.functions.requestTokens(amount).transact()
        self.w3.eth.wait_for_transaction_receipt(tx_hash)

    def get_num_records(self):
        return self.contract.functions.GetNumberOfRecords().call()

    def transfer(self, to, value: int):
        tx_hash = self.contract.functions.transfer(to, value).transact()
        self.w3.eth.wait_for_transaction_receipt(tx_hash)

