import logging


def setup_logger(name: str = __name__) -> logging.Logger:
    """
    Sets up and returns a logger with a standard format and level.
    Logs to console only (file logging optional for later
    """

    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    handler = logging.StreamHandler()
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)  # Change to DEBUG for more detail
    if not logger.handlers:
        logger.addHandler(handler)

    return logger
