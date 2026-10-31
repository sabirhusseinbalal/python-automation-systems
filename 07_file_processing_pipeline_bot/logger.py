import logging

def get_logger(log_file):
    log_file.parent.mkdir(parents=True, exist_ok=True)

    logger = logging.getLogger("bot")
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        formatter = logging.Formatter(
            "%(asctime)s [%(levelname)s] %(message)s"
        )

        for handler in (
            logging.FileHandler(log_file, encoding="utf-8"),
            logging.StreamHandler(),
        ):
            handler.setFormatter(formatter)
            logger.addHandler(handler)

    return logger
