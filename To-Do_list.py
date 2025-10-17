import json
from datetime import datetime

FILE_NAME = "tasks.json"

#Load and save functions-----------------------------------
def load_tasks():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)

    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)


#Add new tasks=--------------------------------------------

def add_task(tasks):
    title = input("Enter task title: ").strip()
    priority = input("Enter task priority(High/Medium/Low): ").strip().capitalize()
    due_date = input("Enter task due date(YYYY-MM-DD): ").strip()

    task = {
        "title": title,
        "priority" : priority if priority else "medium",
        "due_date" : due_date if due_date else "N/A",
        "status" : "Pending"
            }

    tasks.append(task)
    save_tasks(tasks)
    print(f"{task['title']} has been added to the tasks list.")


def view_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return
    print("==========================To Do List:=====================")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}.Title : {task['title']}")
        print(f" Priority : {task['priority']}")
        print(f" Due Date : {task['due_date']}")
        print(f" Status : {task['status']}")
    print()

def update_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return

    view_tasks(tasks)

    try:
        choice = int(input("Enter the number of the task to update: "))
        if choice < 1 or choice > len(tasks):
            print("Invalid choice, please enter a number.\n")
            return

        task = tasks[choice-1]
        print("\nWhat do you want to update?")
        print("1. Title")
        print("2. Priority")
        print("3. Due Date")
        print("4. Status (Pending/Completed)")

        option = input("Enter Your Choice(1-4): ").strip()
        if option == "1":
            task["title"] = input("Enter new task title: ").strip()
        elif option == "2":
            task["priority"] = input("Enter new task priority: ").strip()
        elif option == "3":
            task["due_date"] = input("Enter new task due date: ").strip()
        elif option == "4":
            status = input("Enter new task status(Pending/Completed): ").strip()
            if status in ("Pending", "Completed"):
                task["status"] = status
            else:
                print("Invalid value.\n")
        else:
            print("Invalid choice.\n")

        save_tasks(tasks)
        print(f"{task['title']} has been updated.")

    except ValueError:
        print("Invalid choice.\n")


def delete_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return

    view_tasks(tasks)
    try:
        choice = int(input("Enter the number of the task to delete: "))
        if choice < 1 or choice > len(tasks):
            print("Invalid choice, please enter a number.\n")
            return

        remove_task = tasks.pop(choice-1)
        save_tasks(tasks)
        print(f"{remove_task['title']} has been deleted.")

    except ValueError:
        print("Invalid choice.\n")


def main():
    tasks = load_tasks()

    while True:
        print("\n To-Do List\n")
        print("1. Add task")
        print("2. View tasks")
        print("3. Update tasks")
        print("4. Delete tasks")
        print("5. Exit")
        choice = input("Enter Your Choice(1-5): ").strip()

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            update_tasks(tasks)
        elif choice == "4":
            delete_tasks(tasks)
        elif choice == "5":
            print("Thank you for using To-Do List.")
            break
        else:
            print("Invalid choice.\n")
            return


if __name__ == "__main__":
    main()




