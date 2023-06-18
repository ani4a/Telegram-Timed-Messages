import logging


def log() -> logging.Logger:
    logging.basicConfig(
        format="%(asctime)s - %(message)s",
        level=logging.WARNING,
    )
    return logging.getLogger(__name__)
