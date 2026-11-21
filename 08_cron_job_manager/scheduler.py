from apscheduler.schedulers.blocking import BlockingScheduler
from tasks import get_task
from storage import load_jobs

def run_scheduler(jobs_file):
    scheduler = BlockingScheduler()
    data = load_jobs(jobs_file)

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
        except Exception as e:
            print(f"REJECTED: {e}")


    scheduler.start()  

