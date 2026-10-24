import csv
from pathlib import Path

from sender import send_email


BASE_DIR = Path(__file__).resolve().parent
CSV_FILE = BASE_DIR / "data.csv"
HTML_FILE = BASE_DIR / "index.html"

REQUIRED_COLUMNS = {
    "email",
    "name",
    "topic",
    "resource_url",
}


def main():
    # Read recipient data.
    with CSV_FILE.open("r", encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)

        if not REQUIRED_COLUMNS.issubset(reader.fieldnames or []):
            raise ValueError(
                f"CSV must contain these columns: "
                f"{', '.join(sorted(REQUIRED_COLUMNS))}"
            )

        recipients = list(reader)

    # Read the HTML template.
    html_template = HTML_FILE.read_text(encoding="utf-8")

    if not recipients:
        print("No recipients found in data.csv.")
        return

    print(f"Recipients loaded: {len(recipients)}")
    print("Email sending has not started yet.")

    confirmation = input(
        "Type SEND to send these emails: "
    ).strip()

    if confirmation != "SEND":
        print("Cancelled. No emails were sent.")
        return

    sent = 0
    failed = 0

    for recipient in recipients:
        try:
            # Check that this row has the required values.
            if any(
                not recipient.get(column, "").strip()
                for column in REQUIRED_COLUMNS
            ):
                raise ValueError("A required CSV field is empty.")

            send_email(
                receiver_email=recipient["email"].strip(),
                name=recipient["name"].strip(),
                topic=recipient["topic"].strip(),
                resource_url=recipient["resource_url"].strip(),
                html_template=html_template,
            )

            sent += 1
            print(f"Sent: {recipient['email']}")

        except Exception as error:
            failed += 1
            print(
                f"Failed: {recipient.get('email', 'Unknown recipient')} "
                f"| {error}"
            )

    print("\n--- Sending Summary ---")
    print(f"Successful: {sent}")
    print(f"Failed: {failed}")
    print(f"Total: {len(recipients)}")


if __name__ == "__main__":
    main()