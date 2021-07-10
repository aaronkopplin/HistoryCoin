import json
from web3 import Web3


def deploy():
    w3 = Web3(Web3.HTTPProvider("HTTP://127.0.0.1:7545"))
    w3.eth.defaultAccount = w3.eth.accounts[0]

    if __name__ == "__main__":
        filename = "HistoryCoinAbiBin.json"
    else:
        # print(__name__)
        filename = "SmartContract/CompilingAndDeploying/HistoryCoinAbiBin.json"
    contract_json = open(filename)
    data = json.load(contract_json)
    abi = data["contracts"]["../HistoryCoin.sol:HistoryCoin"]["abi"]
    bytecode = data["contracts"]["../HistoryCoin.sol:HistoryCoin"]["bin"]
    w3_contract = w3.eth.contract(abi=abi, bytecode=bytecode)

    # deploy
    tx_hash = w3_contract.constructor().transact()
    tx_receipt = w3.eth.waitForTransactionReceipt(tx_hash)
    deployed_contract = w3.eth.contract(address=tx_receipt.contractAddress, abi=abi)

    # write the address to a file
    if __name__ == "__main__":
        contract_address_file = open("HistoryCoinContractAddress", "w")
    else:
        contract_address_file = open("SmartContract/CompilingAndDeploying/HistoryCoinContractAddress", "w")
    contract_address_file.write(deployed_contract.address)

    if __name__ == "__main__":
        print("deployed")


if __name__ == "__main__":
    deploy()
