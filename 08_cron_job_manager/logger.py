# Section 1: imports
import logging
from config import LOG_FILE, LOG_DIR


LOG_DIR.mkdir(parents=True, exist_ok=True)   

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,     
    format="%(asctime)s | %(levelname)s | %(message)s",
    filemode="a",   
)


logger = logging.getLogger("cron_job_manager")
