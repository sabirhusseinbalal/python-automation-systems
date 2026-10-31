import csv
import json
import shutil

from dataclasses import dataclass
from pathlib import Path

from config import STAGING_PATH


@dataclass
class ProcessResult:
    success: bool
    output_file: Path | None = None
    transformed: bool = False
    message: str = ""


def file_process(file, category):

    try:
        STAGING_PATH.mkdir(parents=True, exist_ok=True)

        # Text processing
        if category == "text":

            content = file.read_text(encoding="utf-8")

            # Remove unnecessary surrounding whitespace
            content = content.strip()

            output_file = STAGING_PATH / file.name

            output_file.write_text(
                content + "\n",
                encoding="utf-8"
            )

            return ProcessResult(
                True, output_file, True, "Text cleaned"
            )

        # JSON processing
        elif category == "data" and file.suffix.lower() == ".json":

            with file.open("r", encoding="utf-8") as f:
                data = json.load(f)

            output_file = STAGING_PATH / file.name

            with output_file.open("w", encoding="utf-8") as f:
                json.dump(data, f, indent=4, ensure_ascii=False)

            return ProcessResult(
                True, output_file, True, "JSON formatted"
            )

        # CSV processing
        elif category == "data" and file.suffix.lower() == ".csv":

            with file.open("r", encoding="utf-8-sig", newline="") as f:
                reader = csv.DictReader(f)
                rows = list(reader)
                columns = reader.fieldnames

            # Remove unnecessary spaces from values
            cleaned_rows = []

            for row in rows:
                cleaned_row = {
                    key: value.strip() if isinstance(value, str) else value
                    for key, value in row.items()
                }

                cleaned_rows.append(cleaned_row)

            output_file = STAGING_PATH / file.name

            with output_file.open("w", encoding="utf-8", newline="") as f:
                writer = csv.DictWriter(f, fieldnames=columns)
                writer.writeheader()
                writer.writerows(cleaned_rows)

            return ProcessResult(
                True, output_file, True, "CSV cleaned"
            )

        # Other supported files: copy without changing content
        else:

            output_file = STAGING_PATH / file.name

            shutil.copy2(file, output_file)

            return ProcessResult(
                True, output_file, False, "File copied"
            )

    except (OSError, UnicodeError, ValueError, csv.Error) as e:

        return ProcessResult(
            False, None, False, str(e)
        )