import logging
import time
from pathlib import Path


# Parent Folder
BASE_DIR = Path(__file__).resolve().parent
LOG_DIR = BASE_DIR / "logs" # Log Folder
LOG_FILE = LOG_DIR / "bot.log" # Log file

# 1st Class | Logger
class Logger:

    def __init__(self, log_file):
        self.log_file = log_file

        self.log_file.parent.mkdir(parents=True, exist_ok=True)

        self.logger = logging.getLogger("telegram_bot")

        if not self.logger.handlers:
            self.logger.setLevel(logging.INFO)

            formatter = logging.Formatter(
                "%(asctime)s [%(levelname)s] %(message)s"
            )

            file_handler = logging.FileHandler(
                self.log_file,
                mode="a",
                encoding="utf-8"
            )

            console_handler = logging.StreamHandler()

            file_handler.setFormatter(formatter)
            console_handler.setFormatter(formatter)

            self.logger.addHandler(file_handler)
            self.logger.addHandler(console_handler)

    # [INFO]
    def info(self, message):
        self.logger.info(message)

    # [WARNING]
    def warning(self, message):
        self.logger.warning(message)

    # [ERROR]
    def error(self, message):
        self.logger.error(message)

    # [CRITICAL]
    def critical(self, message):
        self.logger.critical(message)

    # Few Seconds hold
    def wait(self):
        for _ in range(3):
            print(".", end="", flush=True)
            time.sleep(1)

        print()