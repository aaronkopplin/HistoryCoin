def my_assert(actual, expected, error_message):
    if actual != expected:
        print("FAILED: " + error_message)
        return False

    return True


def test_all(tests: list):
    successful_tests = 0
    for test in tests:
        passed = test()
        if passed:
            successful_tests += 1

    if successful_tests == len(tests):
        print("all tests passed")
    else:
        print(str(successful_tests) + " passed, " + str(len(tests) - successful_tests) + " failed.")