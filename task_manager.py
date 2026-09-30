from storage import save_tasks, load_tasks

tasks = load_tasks()

def add_task():
    task = input("Enter your task: ")
    tasks.append(task)
    save_tasks(tasks)

def view_tasks():
    for task in tasks:
        print(task)

def delete_task():
    task = input("Enter your task: ")
    try:
        tasks.remove(task)
        save_tasks(tasks)
    except ValueError:
        print("This task does not exist.")

def edit_task():
    try:
        old_task = input("Enter your edit task: ")
        index = tasks.index(old_task)
        new_task = input("Enter your new task: ")
        tasks[index] = new_task
        save_tasks(tasks)

    except ValueError:
        print("This task does not exist.")




while True:
    print("=====TASK MANAGER======")
    print("1. Add task")
    print("2. View tasks")
    print("3. Delete task")
    print("4. Edit task")
    print("5. Exit")

    try:
        choice = int(input("Enter your choice: "))

        if choice < 1 or choice > 5:
            print("Invalid choice. Please enter a valid choice.")

    except ValueError:
        print("Invalid choice. Please enter a valid choice.")
        continue

    if choice == 1:
        add_task()
    elif choice == 2:
        view_tasks()
    elif choice == 3:
        delete_task()
    elif choice == 4:
        edit_task()
    elif choice == 5:
        exit()

