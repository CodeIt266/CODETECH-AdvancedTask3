import logging

def setup_logger():
    logger = logging.getLogger('pen_test_toolkit')
    handler = logging.FileHandler('toolkit.log')
    formatter = logging.Formatter('%(asctime)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)
    return logger

logger = setup_logger()

