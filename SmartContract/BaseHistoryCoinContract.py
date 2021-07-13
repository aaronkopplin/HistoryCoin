from SmartContract.CompilingAndDeploying.deploy import deploy
import json
from web3 import Web3


class BaseHistoryCoinContract:
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
