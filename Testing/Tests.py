from SmartContract.HistoryCoinContract import HistoryCoinContract

contract = HistoryCoinContract()
contract.set_message("hello test")
print(contract.get_message())