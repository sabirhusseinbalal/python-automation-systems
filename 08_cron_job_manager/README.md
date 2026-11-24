# Cron Job Manager

## Description

A simple cron job manager that handles your task schedules, built with Python.

It loads registered jobs from a JSON file, runs them on their configured cron or interval schedules, and records every execution to a log file.

---

## What this project does

- Add a new scheduled job with a name, task, and schedule
- List all registered jobs
- Remove a job by id
- Run a job immediately, outside the scheduler
- Start the scheduler loop to run all jobs on their schedules

---

## Modules Used

- `pathlib` – Handles file and folder paths
- `json` – Reads and writes job configurations
- `logging` – Records scheduler activity
- `argparse` – Parses command-line commands
- `APScheduler` – Runs jobs on schedules

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
4. For help, run:
   python main.py -h
   python main.py add -h

**Note:** This is a beginner level project. Tasks are stubs that print a message, and the focus is on the scheduling infrastructure, not the task content.
