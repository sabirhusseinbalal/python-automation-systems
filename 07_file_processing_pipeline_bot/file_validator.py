import json
import csv

from config import MAX_FILE_SIZE


def file_validator(file, category):

    try:
        # Check whether file exists
        if not file.exists():
            print(f"File does not exist: {file.name}")
            return False

        # Reject symbolic links
        if file.is_symlink():
            print(f"Symbolic link not allowed: {file.name}")
            return False

        # Check whether it is a regular file
        if not file.is_file():
            print(f"Invalid file: {file.name}")
            return False

        # Check file size
        if file.stat().st_size == 0:
            print(f"Empty file: {file.name}")
            return False

        if file.stat().st_size > MAX_FILE_SIZE:
            print(f"File is too large: {file.name}")
            return False

        # Check whether Python can access the file
        with file.open("rb") as f:
            f.read(1)

        # Validate text files
        if category == "text":
            with file.open("r", encoding="utf-8") as f:
                f.read()

        # Validate JSON
        elif category == "data" and file.suffix.lower() == ".json":
            with file.open("r", encoding="utf-8") as f:
                json.load(f)

        # Validate CSV
        elif category == "data" and file.suffix.lower() == ".csv":

            required_columns = {
                "order_id", "product", "quantity", "unit_price"
            }

            with file.open("r", encoding="utf-8-sig", newline="") as f:
                reader = csv.DictReader(f)

                if not reader.fieldnames:
                    print(f"CSV has no header: {file.name}")
                    return False

                actual_columns = set(reader.fieldnames)

                if not required_columns.issubset(actual_columns):
                    print(f"Required columns missing: {file.name}")
                    return False

        return True

    except (OSError, UnicodeError, json.JSONDecodeError, csv.Error) as e:
        print(f"Validation failed for {file.name}: {e}")
        return False