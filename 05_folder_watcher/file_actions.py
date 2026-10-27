import time
from watchdog.observers import Observer

from config import SOURCE_PATH, LOG_FILE
from event_handler import FolderEventHandler
from logger import get_logger


class FolderWatcher:
    def __init__(self):
        self.logger = get_logger(LOG_FILE)
        self.observer = Observer()

    def start(self):
        if not SOURCE_PATH.is_dir():
            self.logger.error(f"Folder not found: {SOURCE_PATH}")
            return

        handler = FolderEventHandler(self.logger)
        self.observer.schedule(
            handler, str(SOURCE_PATH), recursive=True
        )
        self.observer.start()

        self.logger.info(f"Monitoring started: {SOURCE_PATH}")
        self.logger.info("Press Ctrl+C to stop.")

        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            self.logger.info("Stopping monitoring...")
        finally:
            self.observer.stop()
            self.observer.join()
            self.logger.info("Monitoring stopped.")
