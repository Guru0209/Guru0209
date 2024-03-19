# test_suites/test_suite_1.py

import unittest
from tests.testcases.test_login import TestLogin
from tests.testcases.test_logout import TestCheckout

def suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(TestLogin))
    test_suite.addTest(unittest.makeSuite(TestCheckout))
    return test_suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    test_suite = suite()
    runner.run(test_suite)
