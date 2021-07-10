from TestFunctions import Test
from SmartContract.HistoryCoinContract import HistoryCoinContract

contract = HistoryCoinContract()
Test = Test()


def test1():
    contract.set_message("hello test")
    Test.assert_true(contract.get_message(), "hello test", "set_message")


def test2():
    num_records = contract.num_records()
    contract.create_record("test", 2)
    Test.assert_true(contract.num_records(), num_records + 1, "create_record")


def test3():
    contract.redeploy()
    num_records = contract.num_records()
    Test.assert_true(num_records, 0, "num_records")


if __name__ == "__main__":
    tests = [test1, test2, test3]
    Test.test_all(tests)

