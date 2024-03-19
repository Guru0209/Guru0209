# utils/logger.py

import logging
from Config import config

# Configure logging
logging.basicConfig(filename='server-soap.1.log',
        level=logging.INFO,
        format='%(asctime)s %(levelname)s %(threadName)-10s %(message)s',)

# Define a logger
logger = logging.getLogger(__name__)
