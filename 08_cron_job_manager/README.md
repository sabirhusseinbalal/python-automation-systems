# Cron Job Manager

## Description

A simple cron job manager that handles your task schedules, built with Python.

It loads registered jobs from a JSON file, runs each task on its configured cron or interval schedule, and records every action to a log file.

---

## What this project does

- Add a new job with a name, task, schedule type, and trigger arguments
- List all registered jobs
- Remove a job by its id
- Run a single job immediately, without starting the scheduler
- Start the scheduler loop so all jobs run on their own schedules

---

## Modules Used

- `pathlib` – Handles file and folder paths
- `json` – Reads and writes job configurations
- `logging` – Records scheduler activity
- `argparse` – Parses command-line commands
- `APScheduler` – Runs tasks on schedules

---

## Project Structure

```text
08_cron_job_manager/
├── main.py
├── config.py
├── storage.py
├── scheduler.py
├── tasks.py
├── logger.py
├── data/
│   └── jobs.json
├── logs/
│   └── scheduler.log
├── requirements.txt
└── README.md
```

---

## How to Run

1. Make sure Python 3.10 or newer is installed.

2. Install dependencies:

   pip install -r requirements.txt

3. Run a command:

   python main.py list
   python main.py add --name "Morning Report" --task report_task --trigger-type cron --args "{\"hour\": 8, \"minute\": 0}"
   python main.py run-now job_001
   python main.py start

4. See help:

   python main.py -h
   python main.py add -h

**Note:** This is a beginner-level project. Tasks are stubs that print a message, and the focus is on the scheduling infrastructure.
