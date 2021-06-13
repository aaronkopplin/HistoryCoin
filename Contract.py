from solcx import compile_source
from web3 import Web3


def compile_contract(file_path: str, file_name: str, contract_name: str):
    with open(file_path) as contract_file:
        contract_code = contract_file.read()
        compiled_contract = compile_source(contract_code, optimize=True, optimize_runs=9999)
        abi = compiled_contract['<stdin>:Metallic']['abi']
        bytecode = compiled_contract['<stdin>:Metallic']['bin']

        return bytecode, abi


def compile_and_deploy_contract(file_path: str, file_name: str, contract_name: str, w3: Web3):
    bytecode, abi = compile_contract(file_path, file_name, contract_name)

    w3.eth.defaultAccount = w3.eth.accounts[0]
    w3Contract = w3.eth.contract(abi=abi, bytecode=bytecode)
    tx_hash = w3Contract.constructor().transact()
    tx_receipt = w3.eth.waitForTransactionReceipt(tx_hash)
    smart_contract = w3.eth.contract(address=tx_receipt.contractAddress, abi=abi)

    with open('SmartContract/ContractMetaData.py', 'w') as contract_metadata_file:
        contract_metadata_file.write("abi = " + str(abi) + "\n")
        contract_metadata_file.write("address = \"" + str(tx_receipt.contractAddress) + "\"")

    return smart_contract, abi


class HistoryCoinContract:
    def __init__(self):
        self.w3 = Web3()