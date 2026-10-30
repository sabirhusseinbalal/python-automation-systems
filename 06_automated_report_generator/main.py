from data_processor import data_processing
from report_generator import generate_report


def main():

    result = data_processing()

    if result is None:
        print("Report generation stopped: Data processing failed.")
        return

    generate_report(result)


if __name__ == "__main__":
    main()
