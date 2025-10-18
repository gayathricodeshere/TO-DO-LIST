import os

FILE_NAME = "todo_list.txt"

def load_tasks():
    """Load tasks from a file."""
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            tasks = [line.strip() for line in file]
            return tasks
    return []

def save_tasks(tasks):
    """Save tasks to a file."""
    with open(FILE_NAME, "w") as file:
        file.writelines(f"{task}\n" for task in tasks)

def view_tasks(tasks):
    """View all tasks."""
    if not tasks:
        print("\nYour to-do list is empty.\n")
    else:
        print("\nYour To-Do List:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
        print()

def add_task(tasks):
    """Add a new task to the list."""
    task = input("Enter a new task: ").strip()
    if task:
        tasks.append(task)
        print(f"Task '{task}' added.\n")
    else:
        print("Task cannot be empty.\n")

def remove_task(tasks):
    """Remove a task by its number."""
    view_tasks(tasks)
    if not tasks:
        return
    try:
        task_number = int(input("Enter the task number to remove: "))
        if 1 <= task_number <= len(tasks):
            removed_task = tasks.pop(task_number - 1)
            print(f"Task '{removed_task}' removed.\n")
        else:
            print("Invalid task number.\n")
    except ValueError:
        print("Please enter a valid number.\n")

def main():
    """Main function to run the To-Do List app."""
    tasks = load_tasks()

    while True:
        print("To-Do List Menu:")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
            save_tasks(tasks)
        elif choice == "3":
            remove_task(tasks)
            save_tasks(tasks)
        elif choice == "4":
            print("Goodbye!")
            save_tasks(tasks)
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()
