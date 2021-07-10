import json
from web3 import Web3

w3 = Web3(Web3.HTTPProvider("HTTP://127.0.0.1:7545"))
w3.eth.defaultAccount = w3.eth.accounts[0]

contract_json = open("HistoryCoinAbiBin.json")
data = json.load(contract_json)
abi = data["contracts"]["../HistoryCoin.sol:HistoryCoin"]["abi"]
bytecode = data["contracts"]["../HistoryCoin.sol:HistoryCoin"]["bin"]
w3_contract = w3.eth.contract(abi=abi, bytecode=bytecode)

# deploy
tx_hash = w3_contract.constructor().transact()
tx_receipt = w3.eth.waitForTransactionReceipt(tx_hash)
deployed_contract = w3.eth.contract(address=tx_receipt.contractAddress, abi=abi)

# write the address to a file
contract_address_file = open("HistoryCoinContractAddress", "w")
contract_address_file.write(tx_receipt.contractAddress)

print("deployed")
