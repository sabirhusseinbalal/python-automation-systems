# File Processing Pipeline Bot

## Description

A file processing automation tool built with Python.

It scans an input folder, detects file types, validates files, and processes them automatically. Processed, failed, and unsupported files are moved into separate folders.

---

## What this project does

- Detects different file types using extensions
- Checks file size and basic file validity
- Cleans text and CSV files
- Formats JSON files
- Organizes processed files into category folders
- Moves failed and unsupported files separately
- Saves processing activity in a log file
- Shows a final processing summary

---

## File Processing

| File Type | Action |
|---|---|
| TXT / MD | Removes surrounding whitespace |
| JSON | Formats JSON with indentation |
| CSV | Removes extra spaces from values and checks required columns |
| Other supported files | Copies without changing content |
| Unsupported files | Moves to the unsupported folder |

**Maximum file size:** 10 MB

---

## Modules Used

- `pathlib` – Handles file and folder paths
- `shutil` – Moves and copies files
- `csv` – Reads and processes CSV files
- `json` – Reads and formats JSON files
- `logging` – Records processing activity
- `dataclasses` – Stores processing results

---

## Project Structure

```text
08_file_processing_pipeline/
├── main.py
├── pipeline.py
├── config.py
├── file_detector.py
├── file_validator.py
├── file_processor.py
├── file_manager.py
├── logger.py
├── input/
├── output/
│   ├── processed/
│   ├── failed/
│   ├── unsupported/
│   └── _staging/
├── logs/
│   └── bot.log
└── README.md
```

---

## How to Run

1. Make sure Python 3.10 or newer is installed.
2. Place your files inside the `input/` folder.
3. Run the program:

   ```bash
   python main.py
   ```

4. Check the `output/` folder for processed, failed, and unsupported files.
5. Check `logs/bot.log` for processing activity.

**Note:** Files are moved from the input folder during processing. Test with sample files before using important data.
