from apscheduler.schedulers.blocking import BlockingScheduler
from tasks import get_task
from storage import load_jobs
from logger import logger

def run_scheduler(jobs_file):
    scheduler = BlockingScheduler()
    data = load_jobs(jobs_file)

    registered_count = 0

    for item in data:

        try:
            func = get_task(item["task"]) 
            scheduler.add_job(
                func,
                trigger=item["trigger_type"],
                id=item["id"],
                name=item["name"],
                **item["trigger_args"]
            )
            registered_count+=1
        except Exception as e:
            print(f"REJECTED: {e}")
            logger.warning("REJECTED %s", e)

    logger.info("Scheduler started with %d jobs", registered_count)
    scheduler.start()  

