from datetime import datetime

from apscheduler.schedulers.background import BackgroundScheduler
from flask import Flask

from backup import create_backup
from config import BACKUP_INTERVAL_SECONDS


app = Flask(__name__)


@app.route("/")
def home():
    return "<h1>Scheduled Backup System is running.</h1>"


def main():
    print(f"Backup job started: {datetime.now()}")

    result = create_backup()

    if result is None:
        print("Backup job finished with errors.")
    else:
        print("Backup job finished successfully.")


if __name__ == "__main__":
    scheduler = BackgroundScheduler()

    scheduler.add_job(
        main,
        trigger="interval",
        seconds=BACKUP_INTERVAL_SECONDS,
        id="scheduled_backup",
        max_instances=1,
    )

    scheduler.start()

    try:
        app.run(debug=True, use_reloader=False)
    finally:
        scheduler.shutdown(wait=False) # Close