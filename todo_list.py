
tasks = []


def display_menu():
    print("\n--- Todo List Menu ---")
    print("1. View tasks")
    print("2. Add a task")
    print("3. Mark a task as done")
    print("4. Delete a task")
    print("5. Save tasks to a file")
    print("6. Exit")


def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1-6): ")
        if choice == '1':
            view_tasks()
        elif choice == '2':
            add_task()
        elif choice == '3':
            mark_task_done()
        elif choice == '4':
            delete_task()
        elif choice == '5':
            save_tasks_to_file()
        elif choice == '6':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Function placeholders
def view_tasks():
    if not tasks:
        print("No tasks in the list.")
    else:
        print("\n--- Task List ---")
        for i, task in enumerate(tasks, start=1):
            status = "Done" if task['done'] else "Not Done"
            print(f"{i}. {task['name']} [{status}]")


def add_task():
    task_name = input("Enter the task name: ")
    tasks.append({"name": task_name, "done": False})
    print(f"Task '{task_name}' added.")


def mark_task_done():
    view_tasks()
    if not tasks:
        return  # Exit if no tasks exist

    try:
        task_number = int(input("Enter the task number to mark as done: "))
        if 1 <= task_number <= len(tasks):
            tasks[task_number - 1]['done'] = True
            print(f"Task '{tasks[task_number - 1]['name']}' marked as done.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")


def delete_task():
    view_tasks()
    if not tasks:
        return  # Exit if no tasks exist

    try:
        task_number = int(input("Enter the task number to delete: "))
        if 1 <= task_number <= len(tasks):
            deleted_task = tasks.pop(task_number - 1)
            print(f"Task '{deleted_task['name']}' deleted.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")



def save_tasks_to_file():
    file_name = input("Enter the file name to save tasks (e.g., tasks.txt): ")
    try:
        with open(file_name, 'w') as file:
            for task in tasks:
                status = "Done" if task['done'] else "Not Done"
                file.write(f"{task['name']} [{status}]\n")
        print(f"Tasks saved to '{file_name}'.")
    except Exception as e:
        print(f"Error saving tasks: {e}")


if __name__ == "__main__":
    main()
