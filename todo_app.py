
tasks = []
def show_tasks():
    if not tasks:
        print("\nNo tasks available!")
    else:
        print("\n--- YOUR TO-DO LIST ---")
        for i, task in enumerate(tasks, 1):
            status = "✓" if task["done"] else " "
            print(f"{i}. [{status}] {task['name']}")

def add_task():
    name = input("Enter task: ")
    tasks.append({"name": name, "done": False})
    print("Task added successfully!")

def complete_task():
    show_tasks()
    try:
        num = int(input("Enter task number to complete: "))
        tasks[num - 1]["done"] = True
        print("Task completed!")
    except (ValueError, IndexError):
        print("Invalid task number!")

def delete_task():
    show_tasks()
    try:
        num = int(input("Enter task number to delete: "))
        removed = tasks.pop(num - 1)
        print(f"Deleted: {removed['name']}")
    except (ValueError, IndexError):
        print("Invalid task number!")
while True:
    print("\n===== TO-DO APP =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Exit")
    choice = input("Choose an option: ")
    if choice == "1":
        add_task()
    elif choice == "2":
        show_tasks()
    elif choice == "3":
        complete_task()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice! Try again.")
