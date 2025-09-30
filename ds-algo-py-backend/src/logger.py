import logging
import sys

def setup_logger():
    logger = logging.getLogger()  # root logger
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(logging.Formatter(
            "[%(asctime)s] [%(levelname)s] %(name)s: %(message)s",
            "%Y-%m-%d %H:%M:%S"
        ))
        logger.addHandler(console_handler)

    return logger

logger = setup_logger()
