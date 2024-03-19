# test_cases/test_login.py

import unittest
from selenium import webdriver
from Config import config
from Utils.logger import logger

class TestLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(config.DRIVER_PATH)
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(config.ELEMENT_TIMEOUT)

    def test_successful_login(self):
        logger.info("Executing test_successful_login...")
        self.driver.get(config.BASE_URL)
        # Your login test steps here
        pass

    def test_invalid_credentials(self):
        logger.info("Executing test_invalid_credentials...")
        self.driver.get(config.BASE_URL)
        # Your test steps for invalid credentials here
        pass

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()
