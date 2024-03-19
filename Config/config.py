# config.py

class Config:
    # Webdriver settings
    DRIVER_PATH = 'C:\Chrome\chromedriver'
    BROWSER = 'chrome'  # Options: 'chrome', 'firefox', 'edge', etc.

    # Base URL for the application under test
    BASE_URL = 'www.google.com'

    # Credentials for login tests
   # USERNAME = 'testuser'
#    PASSWORD = 'password123'

    # Timeout settings
    PAGE_LOAD_TIMEOUT = 30  # Maximum time to wait for a page to load
    ELEMENT_TIMEOUT = 10    # Maximum time to wait for an element to appear

    # Reporting settings
    REPORT_PATH = 'C:/reports/automation_report.html'

    # Logging settings
    LOG_PATH = 'C:/logs/automation.log'
    LOG_LEVEL = 'INFO'  # Options: 'DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'
