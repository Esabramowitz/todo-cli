import os
import json
import sys

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

def invalid_input():
    print("Invalid input.")
    print("This program expects at least 2 inputs:")
    print("1. Command (add, list, done, delete)")
    print("2. Optional data (required for add, done, delete)")
    return

def main():
    tasks = load_tasks()

    if len(sys.argv) < 2:
        invalid_input()
        return
    
    command = sys.argv[1] #Valid options will be: add, done, list, delete

    if command == "add":
        if len(sys.argv) < 3:
            invalid_input()
            return

        text = " ".join(sys.argv[2:])
        tasks = add_task(tasks, text)
        save_tasks(tasks)
        print(f"Added: {text}")

    elif command == "list":
        pending = [t for t in tasks if not t["done"]] #pending is incomplete tasks

        if len(pending) == 0:
            print("No tasks")
            return

        for t in pending:
            #added incase we want to include compelted tasks later on
            status = "[x]" if t["done"] else "[ ]" 

            print(f'{t["id"]}. {status} {t["text"]}')


    elif command == "done":
        if len(sys.argv) < 3:
            invalid_input()
            return

        task_ids = [int(x) for x in sys.argv[2:]]

        for t in tasks:
            if t["id"] in task_ids:
                t["done"] = True
                print(f"Completed task {t['id']}")

        save_tasks(tasks)


    elif command == "delete":
        if len(sys.argv) < 3:
            invalid_input()
            return

        task_ids = [int(x) for x in sys.argv[2:]]

        # keep only tasks whose id is NOT in the delete list
        tasks = [t for t in tasks if t["id"] not in task_ids]

        for tid in task_ids:
            print(f"Deleted task {tid}")

        save_tasks(tasks)

    else:
        invalid_input()
        
    return


if __name__ == "__main__":
    main()