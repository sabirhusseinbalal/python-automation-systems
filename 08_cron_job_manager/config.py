from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"

JOBS_FILE = DATA_DIR / "jobs.json"

LOG_DIR = BASE_DIR / "logs"
LOG_FILE = LOG_DIR / "scheduler.log"