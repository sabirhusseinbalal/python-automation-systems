from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

SOURCE_PATH = BASE_DIR / "incoming" # Folder for Watch
LOG_FILE = BASE_DIR / "logs" / "bot.log" # Log file
