#Task 1: To-Do-List 
#To-Do-List 
#variables: idx= ID number of the task
#           task_id: id of the task

def show_menu():
    print("\nTo-Do List Menu:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Done")
    print("4. Exit\n")

def add_task(tasks, task):
    tasks.append({"task": task, "done": False})
    print("Task added!\n\n")

def view_tasks(tasks):
    if not tasks:
        print("\nNo tasks found.\n")
        return

    print("\n\nTasks:")
    for idx, task in enumerate(tasks, start=1):
        status = "Done" if task["done"] else "Not Done"
        print(f"{idx}. {task['task']} - {status}")

def mark_task_done(tasks, task_idx):
    if 1 <= task_idx <= len(tasks):
        tasks[task_idx - 1]["done"] = True
        print("\nTask marked as done!\n\n")
    else:
        print("\nInvalid task index.\n\n")

def main():
    tasks = []

    while True:
        show_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter the task: ")
            add_task(tasks, task)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            task_idx = int(input("Enter the task index to mark as done: "))
            mark_task_done(tasks, task_idx)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n\n")

#This code is used to run code inside the if statement while running.
if __name__ == "__main__":
    main()
