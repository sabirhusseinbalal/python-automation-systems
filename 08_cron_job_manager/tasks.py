def generate_report():
    print("[Report]: Generating morning report...")

def run_backup():
    print("[Backup]: Running backup...")

def check_folder():
    print("[Folder]: Checking folder...")

TASKS = {
    "report_task":generate_report,
    "backup_task":run_backup,
    "folder_check_task":check_folder
}


def get_task(name):

    if name not in TASKS:
        raise KeyError(f"Unknown task: '{name}'. Available tasks: {list(TASKS.keys())}")
    
    return TASKS[name]


