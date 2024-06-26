"""Simple To-Do List in Python

This Python script provides a command-line to-do list application with features to:

1.View all tasks (completed and pending)
2.Add new tasks
3.Mark tasks as completed
4.Remove tasks


How to Use:

The program presents a menu with options to manage your to-do list. Simply enter the corresponding number to perform the desired action:

*Display to-do list: View all tasks, including their completion status.
*Add a task: Enter the name of the new task to add it to the list.
*Mark a task as completed: Select a task by its number to mark it as done.
*Remove a task: Choose a task by its number to delete it from the list.
*Quit: Exit the program."""
    
    
    
# Define an empty list to store tasks
tasks = []

# Function to display the to-do list
def display_tasks():
    if not tasks:
        print("Your to-do list is empty.")
    else:
        print("To-Do List:")
        for i, task in enumerate(tasks, start=1):
            status = "Done" if task["completed"] else "Not Done"
            print(f"{i}. {task['task']} ({status})")

# Function to add a task to the to-do list
def add_task():
    task_name = input("Enter the task: ")
    task = {"task": task_name, "completed": False}
    tasks.append(task)
    print(f"Task '{task_name}' added to your to-do list.")

# Function to mark a task as completed
def mark_completed():
    display_tasks()
    task_number = int(input("Enter the task number to mark as completed: "))
    if 1 <= task_number <= len(tasks):
        tasks[task_number - 1]["completed"] = True
        print(f"Task {task_number} marked as completed.")
    else:
        print("Invalid task number. Please enter a valid task number.")

# Function to remove a task from the to-do list
def remove_task():
    display_tasks()
    task_number = int(input("Enter the task number to remove: "))
    if 1 <= task_number <= len(tasks):
        removed_task = tasks.pop(task_number - 1)
        print(f"Task '{removed_task['task']}' removed from your to-do list.")
    else:
        print("Invalid task number. Please enter a valid task number.")

# Main program loop
while True:
    print("\nOptions:")
    print("1. Display to-do list")
    print("2. Add a task")
    print("3. Mark a task as completed")
    print("4. Remove a task")
    print("5. Quit")
    choice = input("Enter your choice: ")

    if choice == '1':
        display_tasks()
    elif choice == '2':
        add_task()
    elif choice == '3':
        mark_completed()
    elif choice == '4':
        remove_task()
    elif choice == '5':
        break
    else:
        print("Invalid choice. Please enter a valid option.")
