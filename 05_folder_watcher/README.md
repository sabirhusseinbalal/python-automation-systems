# Folder Watcher

## Description

A simple folder monitoring tool built with Python and Watchdog.

It watches a selected folder and records when files or folders are created, deleted, or moved. It also logs file modifications.

---

## What this project does

- Monitors a folder and its subfolders
- Detects file and folder changes
- Records events in a log file
- Shows log messages in the terminal
- Stops monitoring when the user presses `Ctrl+C`

---

## Modules Used

- `watchdog` – Monitors file system events
- `logging` – Records activity and errors
- `pathlib` – Handles file and folder paths
- `time` – Keeps the program running

---

## Project Structure

```text
05_folder_watcher/
├── main.py
├── file_actions.py
├── event_handler.py
├── logger.py
├── config.py
├── input/
├── logs/
│   └── folder_watcher.log
├── requirements.txt
└── README.md
```

---

## How to Run

1. Install the required package:

   ```bash
   pip install -r requirements.txt
   ```

2. Create an `input/` folder in the project directory.

3. Run the program:

   ```bash
   python main.py
   ```

4. Create, edit, rename, or delete files inside `input/` and check the terminal or log file.

5. Press `Ctrl+C` to stop monitoring.

**Note:** This version records folder changes but does not yet perform automatic file actions. Moving, organizing, or processing files automatically can be added in a future update.
