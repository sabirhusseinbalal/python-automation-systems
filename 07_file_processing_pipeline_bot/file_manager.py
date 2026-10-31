import shutil

from config import (
    PROCESSED_PATH,
    FAILED_PATH,
    UNSUPPORTED_PATH
)


def get_unique_path(path):

    destination = path
    counter = 1

    while destination.exists():
        destination = path.with_name(
            f"{path.stem}_{counter}{path.suffix}"
        )
        counter += 1

    return destination


def move_to_processed(original_file, result, category):

    try:
        category_folder = PROCESSED_PATH / category
        category_folder.mkdir(parents=True, exist_ok=True)

        if result.transformed:

            # Move the newly processed file
            destination = get_unique_path(
                category_folder / result.output_file.name
            )

            shutil.move(str(result.output_file), str(destination))

            # Keep the original file separately
            originals_folder = PROCESSED_PATH / "originals"
            originals_folder.mkdir(parents=True, exist_ok=True)

            original_destination = get_unique_path(
                originals_folder / original_file.name
            )

            shutil.move(str(original_file), str(original_destination))

        else:

            # Move original file without changing it
            destination = get_unique_path(
                category_folder / original_file.name
            )

            shutil.move(str(original_file), str(destination))

        return True

    except OSError as e:
        print(f"Error moving processed file {original_file.name}: {e}")
        return False


def move_to_failed(file, category="others"):

    try:
        FAILED_PATH.mkdir(parents=True, exist_ok=True)

        destination_folder = FAILED_PATH / category
        destination_folder.mkdir(parents=True, exist_ok=True)

        destination = get_unique_path(
            destination_folder / file.name
        )

        shutil.move(str(file), str(destination))

        return True

    except OSError as e:
        print(f"Error moving failed file: {e}")
        return False


def move_to_unsupported(file):

    try:
        UNSUPPORTED_PATH.mkdir(parents=True, exist_ok=True)

        destination = get_unique_path(
            UNSUPPORTED_PATH / file.name
        )

        shutil.move(str(file), str(destination))

        return True

    except OSError as e:
        print(f"Error moving unsupported file: {e}")
        return False