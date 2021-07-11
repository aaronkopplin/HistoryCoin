import web3.eth

from TestFunctions import Test
from SmartContract.HistoryCoinContract import HistoryCoinContract
from web3 import Web3


Test = Test()
contract = HistoryCoinContract()


def test1():
    contract.set_message("hello test")
    Test.assert_true(contract.get_message(), "hello test", "set_message")


def test2():
    num_records_before = contract.get_num_records()
    contract.create_record("test", 2)
    num_records_after = contract.get_num_records()
    Test.assert_true(num_records_after, num_records_before + 1, "create_record")
    Test.assert_true(contract.get_record_text(num_records_after - 1), "test", "get_record_text")

    num_records_before = contract.get_num_records()
    contract.create_record("another test", 2)
    num_records_after = contract.get_num_records()
    Test.assert_true(num_records_after, num_records_before + 1, "create_record")
    Test.assert_true(contract.get_record_text(num_records_after - 1), "another test", "get_record_text")


def test3():
    contract.redeploy()
    num_records = contract.get_num_records()
    Test.assert_true(num_records, 0, "num_records")


def test4():
    begin_bal = contract.get_balance_of_sender()
    contract.request_tokens(1000)
    new_bal = contract.get_balance_of_sender()
    Test.assert_true(begin_bal + 1000, new_bal, "request_tokens")


def test5():
    new_account = contract.w3.eth.accounts[1]
    old_balance = contract.get_balance_of(new_account)

    contract.request_tokens(100)
    contract.transfer(new_account, 100)
    new_address_balance = contract.get_balance_of(new_account)
    Test.assert_true(new_address_balance, old_balance + 100, "transfer")


def test6():
    contract.redeploy()
    tot_supply = contract.get_total_supply()
    Test.assert_true(tot_supply, 1000000, "get_total_supply")

    contract.request_tokens(100)
    new_tot_supply = contract.get_total_supply()
    Test.assert_true(new_tot_supply, tot_supply + 100, "get_total_supply")


if __name__ == "__main__":
    # test1()
    # test2()
    # test3()
    # test4()
    # test5()
    test6()
    Test.print_diagnostics()

