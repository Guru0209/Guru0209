# test_cases/test_checkout.py

import unittest
from selenium import webdriver
from Config import config
from Utils.logger import logger

class TestCheckout(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(config.DRIVER_PATH)
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(config.ELEMENT_TIMEOUT)

    def test_add_to_cart(self):
        logger.info("Executing test_add_to_cart...")
        self.driver.get(config.BASE_URL)
        # Your checkout test steps here
        pass

    def test_remove_from_cart(self):
        logger.info("Executing test_remove_from_cart...")
        self.driver.get(config.BASE_URL)
        # Your test steps for removing items from cart here
        pass

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()
