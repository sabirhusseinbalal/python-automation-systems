from watchdog.events import FileSystemEventHandler


class FolderEventHandler(FileSystemEventHandler):
    def __init__(self, logger):
        self.logger = logger

    def on_created(self, event):
        self.logger.info(f"[CREATED] {event.src_path}")

    def on_deleted(self, event):
        self.logger.info(f"[DELETED] {event.src_path}")

    def on_modified(self, event):
        if not event.is_directory:
            self.logger.info(f"[MODIFIED] {event.src_path}")

    def on_moved(self, event):
        self.logger.info(
            f"[MOVED] {event.src_path} -> {event.dest_path}"
        )

    def on_any_event(self, event):
        print(super().on_any_event(self.event))
