import os
import json

TASK_FILE = "task.json"

def load_tasks():
    if not os.path.exists.(TASK_FILE)
        with open(TASK_FILE) as f
            json.dump([], f)
        return []
    with open(TASK_FILE, "r") as f:
        return json.load(f)

print("Todo CLI")