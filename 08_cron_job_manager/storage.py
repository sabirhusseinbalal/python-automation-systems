import json

# Load data
def load_jobs(file_path):

    if not file_path.exists():
        return []

    try:
        with file_path.open("r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        print(f"WARNING: {file_path} is corrupted. Starting with empty job list.")
        return []

# Save data
def save_jobs(jobs, file_path):

    with file_path.open("w", encoding="utf-8") as f:
        json.dump(jobs, f, indent=2)
