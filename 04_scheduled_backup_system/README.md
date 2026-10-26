# Scheduled Backup System

## Description

A simple backup automation system built with Python, APScheduler, and Flask.

This is the fourth project in my **Automation Systems & Bots** group. It creates ZIP backups of a folder at regular intervals and keeps previous backups.

---

## What this project does

- Creates ZIP backups of a folder or file
- Runs backups automatically every 30 seconds
- Adds a timestamp to each backup filename
- Keeps previous backups
- Shows backup success or failure in the terminal
- Provides a simple Flask homepage

---

## Modules Used

- `shutil` – Creates ZIP archives
- `pathlib` – Handles file and folder paths
- `datetime` – Adds timestamps to backup filenames
- `APScheduler` – Runs backups at scheduled intervals
- `Flask` – Provides a simple web page

---

## Project Structure

```text
04_scheduled_backup_system/
├── main.py
├── backup.py
├── config.py
├── input/
├── backup/
├── requirements.txt
└── README.md
```

---

## How to Run

1. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

2. Put the files or folders you want to back up inside the `input/` folder.

3. Run the application:

   ```bash
   python main.py
   ```

4. Open this address in your browser:

   `http://127.0.0.1:5000/`

5. Check the `backup/` folder for the generated ZIP files.

**Note:** The first backup runs after the configured interval. The application must remain running for scheduled backups to work.
