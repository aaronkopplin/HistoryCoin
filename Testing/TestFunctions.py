class Test:
    def __init__(self):
        self.count = 0
        self.successful_tests = 0
        self.failures = 0

    def assert_true(self, actual, expected, error_message: str):
        self.count += 1
        if actual != expected:
            print("FAILED: " + error_message + " => EXPECTED: " + str(expected) + ", ACTUAL " + str(actual))
            self.failures += 1
        else:
            self.successful_tests += 1

    def print_diagnostics(self):
        if self.failures == 0:
            print("all (" + str(self.count) + ") assertions passed")
        else:
            print(str(self.successful_tests) + " passed, " + str(self.failures) + " failed.")

