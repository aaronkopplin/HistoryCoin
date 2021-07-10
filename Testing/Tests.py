from TestFunctions import test_all, my_assert
from SmartContract.HistoryCoinContract import HistoryCoinContract

contract = HistoryCoinContract()


def test1():
    contract.set_message("hello test")
    return my_assert(contract.get_message(), "hello test", "test1")


if __name__ == "__main__":
    tests = [test1]
    test_all(tests)

