import sys
import os
import json
from datetime import datetime

FILE_NAME = "tasks.json"

def load_tasks():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w") as f:
            json.dump([], f)
    with open(FILE_NAME, "r") as f:
        return json.load(f)

def save_tasks(tasks):
    with open(FILE_NAME, "w") as f:
        json.dump(tasks, f, indent=2)

def add_task(description):
    tasks = load_tasks()
    new_id = max((task["id"] for task in tasks), default=0) + 1
    task = {
        "id": new_id,
        "description": description,
        "status": "todo",
        "createdAt": datetime.now().isoformat(),
        "updatedAt": datetime.now().isoformat(),
    }
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task added successfully (ID: {new_id})")

# Add handlers for other commands...

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: task-cli <command> [arguments]")
        sys.exit(1)

    command = sys.argv[1]
    if command == "add":
        description = sys.argv[2]
        add_task(description)
    # Handle other commands...
