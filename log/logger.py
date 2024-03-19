# logger.py

import logging
from Config import config

# Configure logging
logging.basicConfig(level=config.LOG_LEVEL,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    filename=config.LOG_PATH,
                    filemode='w')

# Define a logger
logger = logging.getLogger(__name__)

# Example usage:
# logger.info("This is an info message")
# logger.warning("This is a warning message")
# logger.error("This is an error message")
# logger.debug("This is a debug message")
