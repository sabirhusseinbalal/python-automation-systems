# Scheduled Backup System

## Description

A scheduled backup application built with Python, APScheduler, and Flask.

This is the fourth project in the **Automation Systems & Bots** group. The main goal is to understand how Python can automate recurring backup tasks and how a scheduler can work alongside a web application.

The project builds on the Folder Backup Tool from the File & Folder Automation group.

It introduces scheduled execution, ZIP archives, modular code organization, and basic web application integration.

---

## What This Project Does

- Creates ZIP backups of a source folder or file
- Runs backups automatically at scheduled intervals
- Uses timestamped archive filenames
- Preserves previous backups
- Reports backup success and failure
- Provides a simple Flask homepage
- Separates configuration, backup logic, and application startup

---

## How It Works

The basic workflow is:

```text
        main.py
           |
           v
   APScheduler
           |
           v
          main()
           |
           v
       backup.py
           |
           v
     Validate Source
           |
           v
   Create ZIP Archive
           |
           v
      backup/
```

Flask runs alongside the scheduler and serves a simple homepage.

---

## Concepts Learned

### Python

- Functions
- Modules and imports
- Exception handling
- `pathlib`
- File and directory validation
- `datetime`
- ZIP archive creation
- Return values

### Automation

- Scheduled jobs
- Interval-based execution
- Background scheduling
- Preventing overlapping job executions
- Automatic recurring tasks

### Web Development

- Flask application setup
- URL routes
- HTTP requests and responses
- Running a web application alongside a background scheduler

### Project Organization

- Separating responsibilities into modules
- Configuration management
- Dependencies and `requirements.txt`

---

## Project Structure

```text
04_scheduled_backup_system/
│
├── main.py
├── backup.py
├── config.py
├── input/
├── backup/
├── requirements.txt
└── README.md
```

### File Responsibilities

**`main.py`**

Creates the Flask application, defines the homepage, coordinates backup runs, and starts the scheduler.

**`backup.py`**

Validates the source path and creates timestamped ZIP archives.

**`config.py`**

Defines the project directory, source path, backup destination, and scheduling interval.

**`input/`**

Contains the files or folders to back up.

**`backup/`**

Stores the generated ZIP archives.

**`requirements.txt`**

Lists the external Python dependencies.

---

## Configuration

The scheduling interval is defined in `config.py`:

```python
BACKUP_INTERVAL_SECONDS = 30
```

The 30-second interval is intended for testing.

For a 24-hour interval, use:

```python
BACKUP_INTERVAL_SECONDS = 86400
```

The source and backup paths are configured relative to the project directory.

---

## Dependencies

The external dependencies are:

```text
APScheduler
Flask
```

Install them using:

```bash
python -m pip install -r requirements.txt
```

The remaining modules are included in Python's standard library.

---

## Running the Project

1. Install the requirements.
2. Place test files inside the `input/` folder.
3. Run the application:

```bash
python main.py
```

4. Wait for the scheduled backup to run.
5. Open the following address in your browser:

```text
http://127.0.0.1:5000/
```

6. Check the `backup/` directory for the generated ZIP archive.

The scheduler runs only while the Python application is running. The first scheduled backup normally occurs after the configured interval.

---

## Testing

### Tests to Perform

- Create a ZIP archive from a folder.
- Create a ZIP archive from a file.
- Handle a missing source path.
- Verify that archive contents are correct.
- Run multiple scheduled backups.
- Verify that previous archives are preserved.
- Handle compression errors.
- Confirm that the Flask homepage responds successfully.
- Stop the application and verify that scheduling stops.

### Example Output

```text
Backup job started: 2026-10-24 16:50:00
Backup successful: .../backup/input_2026-10-24_16-50-00.zip
Backup job finished successfully.
```

This is illustrative output, not a claim that every test has been performed.

---

## Important Notes

- The application must remain running for scheduled jobs to execute.
- Flask's built-in development server is intended for development, not production deployment.
- Previous backups are retained, so the backup directory can grow over time.
- This version does not implement automatic backup retention or deletion.
- A production deployment would need more robust logging, monitoring, and scheduler lifecycle management.

---

## Learning Outcome

The purpose of this project is to understand how Python can execute recurring automation tasks and how different application responsibilities can be organized into separate modules.

Through this project, I aim to learn how to:

- Create ZIP archives programmatically
- Schedule recurring tasks
- Integrate a background scheduler with Flask
- Organize code into maintainable modules
- Handle basic backup errors
- Preserve historical backup versions

This project is a step toward building more maintainable Python automation systems.

---

## Future Improvements

Possible improvements for later projects:

- Add a web dashboard showing backup status
- Add a button to trigger backups manually
- Support configurable source and destination paths
- Add structured logging
- Add automated tests
- Implement backup retention policies
- Add configurable scheduling options
- Improve error reporting and monitoring
