from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

SOURCE_PATH = BASE_DIR / "input" # Default folder
BACKUP_DIR = BASE_DIR / "backup" # Backup folder

BACKUP_INTERVAL_SECONDS = 30 # Set time