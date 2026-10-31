from config import INPUT_PATH, OUTPUT_PATH, LOG_FILE

from file_detector import file_detector
from file_validator import file_validator
from file_processor import file_process

from file_manager import (
    move_to_processed,
    move_to_failed,
    move_to_unsupported
)

from logger import get_logger


logger = get_logger(LOG_FILE)


def run_pipeline():

    # Create output folder
    OUTPUT_PATH.mkdir(parents=True, exist_ok=True)

    # Check input folder
    if not INPUT_PATH.is_dir():
        logger.error("Input folder does not exist.")
        print("Input folder not found.")
        return

    # Detect files
    files = file_detector(INPUT_PATH)

    if not files:
        print("No files found.")
        logger.info("No files found.")
        return

    # Counters
    total = len(files)
    successful = 0
    failed = 0
    unsupported = 0

    print(f"\nFound {total} files.\n")
    logger.info("Pipeline started. Found %s files.", total)

    # Process each file
    for file, category in files.items():

        print(f"Processing: {file.name}")

        # Unsupported file
        if category == "others":

            if move_to_unsupported(file):
                unsupported += 1
                logger.warning("Unsupported file: %s", file.name)

            continue

        # Validate file
        if not file_validator(file, category):

            if move_to_failed(file, category):
                failed += 1

            logger.warning("Validation failed: %s", file.name)
            continue

        # Process file
        result = file_process(file, category)

        if not result.success:

            if move_to_failed(file, category):
                failed += 1

            logger.error(
                "Processing failed: %s - %s",
                file.name,
                result.message
            )
            continue

        # Move successful file
        if move_to_processed(file, result, category):

            successful += 1

            print(f"Successfully processed: {file.name}")
            logger.info(
                "Successfully processed: %s",
                file.name
            )

        else:

            failed += 1
            logger.error("Could not save processed file: %s", file.name)

    # Final summary
    print("\n========== PIPELINE REPORT ==========")
    print(f"Total files:       {total}")
    print(f"Successful:       {successful}")
    print(f"Failed:           {failed}")
    print(f"Unsupported:      {unsupported}")
    print("=====================================")

    logger.info(
        "Pipeline completed. Total=%s Successful=%s Failed=%s Unsupported=%s",
        total,
        successful,
        failed,
        unsupported
    )