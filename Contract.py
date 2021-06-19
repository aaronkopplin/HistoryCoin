import json
from web3 import Web3


class HistoryCoinContract:
    def __init__(self):
        self.w3 = Web3(Web3.HTTPProvider("HTTP://127.0.0.1:7545"))
        self.w3.eth.defaultAccount = self.w3.eth.accounts[0]

        contract_json = open("HistoryCoinAbiBin.json")
        data = json.load(contract_json)
        abi = data["contracts"]["HistoryCoin.sol:HistoryCoin"]["abi"]

        with open("HistoryCoinContractAddress", "r") as contract_address_file:
            address = contract_address_file.readline()
            self.contract = self.w3.eth.contract(address=address, abi=abi)

    def get_message(self):
        return self.contract.functions.GetMessage().call()

    def set_message(self, message: str):
        tx_hash = self.contract.functions.SetMessage(message).transact()
        tx_receipt = self.w3.eth.wait_for_transaction_receipt(tx_hash)


