import argparse
import json
from config import JOBS_FILE, DATA_DIR, LOG_DIR
from storage import load_jobs, save_jobs
from tasks import get_task, TASKS
from scheduler import run_scheduler
from logger import logger

def cmd_list(args):

    jobs = load_jobs(JOBS_FILE)

    if not jobs:
        print("No jobs registered yet")
        logger.warning("No jobs registered yet")
        return

    for j in jobs:
        try:
            print(f"ID: {j['id']} | Name: {j['name']} | Task: {j['task']} | Trigger: {j['trigger_type']}")
        except KeyError as e:
            print(f"REJECTED: {j.get('id', '?')} - reason {e}")
            logger.error("REJECTED: %s - reason %s", j.get('id', '?'), e)

def cmd_add(args):

    try:
        trigger_args = json.loads(args.args)
    except json.JSONDecodeError as e:
        print(f"Invalid --args JSON: {e}")
        logger.error("REJECTED: invalid --args - %s", e)
        return

    name = args.name
    task = args.task
    trigger_type = args.trigger_type

    jobs = load_jobs(JOBS_FILE)

    numbers = [int(j['id'].split('_')[1]) for j in jobs]
    next_num = max(numbers, default=0) + 1
    new_id = f"job_{next_num:03d}"   

    jobs.append(
            {
        'id': new_id,
        'name': name,
        'task': task,
        'trigger_type': trigger_type,
        'trigger_args': trigger_args
    }
        )

    try:
        save_jobs(jobs, JOBS_FILE)
        print("Saved!")
        logger.info("Added job %s (%s)", new_id, name)
    except IOError as e:
        print(f"Save failed: {e}")
        logger.error("Failed to save job: %s", e)    


def cmd_remove(args):

    jobs = load_jobs(JOBS_FILE)

    if not jobs:
        print("No jobs registered yet")
        logger.warning("No jobs registered yet")
        return
    
    job = next((j for j in jobs if j['id'] == args.job_id), None)
    if job is None:
        print(f"No job with id '{args.job_id}'")
        logger.warning("No job with id %s", args.job_id)
        return

    jobs = [j for j in jobs if j['id'] != args.job_id]

    try:
        save_jobs(jobs, JOBS_FILE)
        print(f"Removed job {args.job_id}")
        logger.info("Removed job %s", args.job_id)
    except IOError as e:
        print(f"Save failed: {e}")
        logger.error("Failed to save jobs: %s", e)    


    

def cmd_run_now(args):
    jobs = load_jobs(JOBS_FILE)
    
    if not jobs:
        print("No jobs registered yet")
        logger.warning("No jobs registered yet")
        return
        
    job = next((j for j in jobs if j['id'] == args.job_id), None)
    if job is None:
        print(f"No job with id '{args.job_id}'")
        logger.warning("No job with id %s", args.job_id)
        return
    
    try:
        func = get_task(job['task'])
    except KeyError as e:
        print(f"REJECTED: {e}")
        logger.warning("Run-now rejected: %s", e)
        return

    try:
        func()
        logger.info("Ran job %s (%s) via run-now", job['id'], job['name'])
        print(f"Ran job '{job['name']}' once.")
    except Exception as e:
        logger.error("Job %s failed: %s", job['id'], e)
        print(f"Job failed: {e}")
        

def cmd_start(args):

    jobs = load_jobs(JOBS_FILE)
    if not jobs:
        print("No jobs registered yet")
        logger.warning("No jobs registered yet")
        return
    
    print(f"Starting scheduler with {len(jobs)} job(s)...")
    logger.info("Starting scheduler with %d jobs", len(jobs))
    run_scheduler(JOBS_FILE)
    


def build_parser():
    parser = argparse.ArgumentParser(prog="cron-job-manager", description="Manage scheduled tasks.")
    sub = parser.add_subparsers(dest="command", required=True)

    # list
    p_list = sub.add_parser("list", help="Show all registered jobs")
    p_list.set_defaults(func=cmd_list)

    # add
    p_add = sub.add_parser("add", help="Register a new job")
    p_add.add_argument("--name", required=True, help="Human-readable job name")
    p_add.add_argument("--task", required=True, choices=list(TASKS.keys()), help="Registered task to run")
    p_add.add_argument("--trigger-type", required=True, choices=["cron", "interval"], help="Schedule type")
    p_add.add_argument("--args", required=True, help='Trigger args as JSON, e.g. \'{"hour": 8, "minute": 0}\'')
    p_add.set_defaults(func=cmd_add)

    # remove
    p_remove = sub.add_parser("remove", help="Remove a job by id")
    p_remove.add_argument("job_id", help="e.g. job_001")
    p_remove.set_defaults(func=cmd_remove)

    # run-now
    p_run = sub.add_parser("run-now", help="Run a job once, right now")
    p_run.add_argument("job_id", help="e.g. job_001")
    p_run.set_defaults(func=cmd_run_now)

    # start
    p_start = sub.add_parser("start", help="Start the scheduler loop")
    p_start.set_defaults(func=cmd_start)

    return parser


def main():
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    LOG_DIR.mkdir(parents=True, exist_ok=True)
    parser = build_parser()
    args = parser.parse_args()
    args.func(args)                          


if __name__ == "__main__":
    main()