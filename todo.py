import os
import json

TASK_FILE = "tasks.json"

def load_tasks():
    if not os.path.exists(TASK_FILE):
        with open(TASK_FILE, "w") as f:
            json.dump([], f)
        return []
    with open(TASK_FILE, "r") as f:
        return json.load(f)

def add_task(tasks, text):
    new_id = len(tasks) + 1
    new_task = {
        "id": new_id,
        "text": text,
        "done": False
    }
    tasks.append(new_task)
    return tasks


def save_tasks(tasks):
    with open(TASK_FILE, "w") as f:
        json.dump(tasks, f, indent=2)


print("Todo CLI")