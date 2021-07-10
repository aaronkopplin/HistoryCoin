class Test:
    def __init__(self):
        self.count = 0
        self.successful_tests = 0

    def assert_true(self, actual, expected, error_message: str):
        self.count += 1
        if actual != expected:
            print("FAILED: " + error_message + " => EXPECTED: " + str(expected) + ", ACTUAL " + str(actual))
            return

        self.successful_tests += 1

    def test_all(self, tests: list):
        failures = 0
        for test in tests:
            before_count = self.count
            before_successes =  self.successful_tests
            test()
            tests_ran = self.count - before_count
            successful_tests_ran = self.successful_tests - before_successes
            if successful_tests_ran < tests_ran:
                failures += 1

        if failures == 0:
            print("all (" + str(len(tests)) + ") tests passed")
        else:
            print(str(len(tests) - failures) + " passed, " + str(failures) + " failed.")