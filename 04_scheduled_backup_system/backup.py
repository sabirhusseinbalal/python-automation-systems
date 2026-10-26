import shutil
from datetime import datetime

from config import SOURCE_PATH, BACKUP_DIR

# fnc
def create_backup():
    if not SOURCE_PATH.exists():
        print(f"Source not found: {SOURCE_PATH}")
        return None

    if not SOURCE_PATH.is_dir() and not SOURCE_PATH.is_file():
        print(f"Invalid source: {SOURCE_PATH}")
        return None

    BACKUP_DIR.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    archive_name = f"{SOURCE_PATH.name}_{timestamp}"
    archive_path = BACKUP_DIR / archive_name

    try:
        result = shutil.make_archive(
            str(archive_path),
            "zip",
            root_dir=SOURCE_PATH.parent,
            base_dir=SOURCE_PATH.name,
        )

        print(f"Backup successful: {result}")
        return result

    except (OSError, shutil.Error) as error:
        print(f"Backup failed: {error}")
        return None