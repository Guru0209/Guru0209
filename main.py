# main.py

import unittest
from tests.testsuite.testsute import suite
from Utils.report import generate_html_report
from Utils.logger import logger

def run_tests():
    logger.info("Starting test execution...")
    test_suite = suite()
    runner = unittest.TextTestRunner()
    result = runner.run(test_suite)
    logger.info("Test execution completed.")

    # Generate HTML report
    generate_html_report(result.__dict__['_tests'])

if __name__ == "__main__":
    run_tests()
