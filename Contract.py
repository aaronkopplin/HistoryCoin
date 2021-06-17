import json
from web3 import Web3


def get_abi():
    contract_json = open("HistoryCoinAbiBin.json")
    data = json.load(contract_json)
    return data["contracts"]["HistoryCoin.sol:HistoryCoin"]["abi"]


def get_binary():
    contract_json = open("HistoryCoinAbiBin.json")
    data = json.load(contract_json)
    return data["contracts"]["HistoryCoin.sol:HistoryCoin"]["bin"]


def deploy_contract(w3: Web3, abi):
    w3_contract = w3.eth.contract(abi=abi, bytecode=get_binary())
    tx_hash = w3_contract.constructor().transact()
    tx_receipt = w3.eth.waitForTransactionReceipt(tx_hash)
    deployed_contract = w3.eth.contract(address=tx_receipt.contractAddress, abi=abi)
    with open("HistoryCoinContractAddress", "w") as contract_address_file:
        contract_address_file.write(tx_receipt.contractAddress)

    return deployed_contract, tx_receipt.contractAddress


class HistoryCoinContract:
    def __init__(self):
        self.w3 = Web3(Web3.HTTPProvider("HTTP://127.0.0.1:7545"))
        self.w3.eth.defaultAccount = self.w3.eth.accounts[0]
        self.abi = get_abi()
        self.contract, self.address = deploy_contract(self.w3, self.abi)
        self.contract = self.w3.eth.contract(self.address)
