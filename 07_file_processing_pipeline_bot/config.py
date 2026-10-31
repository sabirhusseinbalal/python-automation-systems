from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

INPUT_PATH = BASE_DIR / "input" # Input folder
OUTPUT_PATH = BASE_DIR / "output" # Output folder

PROCESSED_PATH = OUTPUT_PATH / "processed" # Processed folder
FAILED_PATH = OUTPUT_PATH / "failed" # failed fail
UNSUPPORTED_PATH = OUTPUT_PATH / "unsupported" # unsupported

STAGING_PATH = OUTPUT_PATH / "_staging"

LOG_PATH = BASE_DIR / "logs"
LOG_FILE = LOG_PATH / "bot.log"

MAX_FILE_SIZE_MB = 10
MAX_FILE_SIZE = MAX_FILE_SIZE_MB * 1024 * 1024
