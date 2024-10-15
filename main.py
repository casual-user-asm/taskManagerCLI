import argparse
from datetime import datetime
import json

parser = argparse.ArgumentParser(description="Your task manager")
current_time = datetime.now()
create_time = current_time.strftime("%H:%M %d.%m.%Y")
update_time = current_time.strftime("%H:%M %d.%m.%Y")


def load_tasks():
    try:
        with open("tasks.json", "r") as file:
            return json.load(file)
    except:  # noqa: E722
        print("Not file found")
        return {}


def save_tasks(tasks):
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)


tasks = load_tasks()

parser.add_argument("--add", type=str, nargs="+", help="Add task")
parser.add_argument("--update", nargs="+", help="Update task")
parser.add_argument("--delete", type=str, help="Delete task")
parser.add_argument("--started", type=str, help="Change status to in progress")
parser.add_argument("--done", type=str, help="Change status in done")
parser.add_argument("--list", help="Type 'show' to see tasks")
parser.add_argument("--clear_list", help="Clear task list")


args = parser.parse_args()
if args.add:
    formatted_task = " ".join(args.add)
    tasks[len(tasks) + 1] = {
        "description": f"{formatted_task}",
        "status": "todo",
        "createdAt": f"{create_time}",
        "updatedAt": "",
    }
    save_tasks(tasks)
    print(f"Task added succesfully. Task ID is {len(tasks)}")
elif args.update:
    update_id = args.update[0]
    new_task = args.update[1]
    tasks[update_id]["description"] = f"{new_task}"
    tasks[update_id]["updatedAt"] = f"{update_time}"
    save_tasks(tasks)
elif args.delete:
    del tasks[f"{args.delete}"]
    save_tasks(tasks)
elif args.started:
    tasks[f"{args.started}"]["status"] = "In progress"
    save_tasks(tasks)
elif args.done:
    tasks[f"{args.done}"]["status"] = "Done"
    save_tasks(tasks)
elif args.list:
    for id, task in tasks.items():
        task_id = id
        print(
            f'Task: {task["description"].capitalize()} | Status: {task["status"].upper()} | Task ID: {task_id}'
        )
elif args.clear_list:
    tasks = {}
    save_tasks(tasks)
