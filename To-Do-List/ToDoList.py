import json

def load_tasks():
    try:
        with open('tasks.json', 'r' ) as file:
            return json.load(file)
    except FileNotFoundError:
        return [] 

def save_tasks(tasks):
    try:
        with open('tasks.json', 'w') as file:
            json.dump(tasks, file)
    except FileNotFoundError:
        return 'File not found!'

def add_task(tasks, task):
    tasks.append({'task':task,'completed':False})

def view_tasks(tasks):
    if not tasks:
        print('Warning: You have not added any tasks.')
    for idx, task in enumerate(tasks, start=1):
        print(f"[{idx}]{' > X <' if task['completed'] else '  ' } {task['task']}")


def remove_task(tasks, idx):
    if idx >= 0 and idx < len(tasks):
        del tasks[idx]
    else:
        print('Warning: Invalid task index given.')

def complete_task(tasks, idx):
    if idx >= 0 and idx < len(tasks):
        tasks[idx]['completed'] = True
    else:
        print('Warning: Invalid task index given.')
    



def main():
    tasks = load_tasks()

    while True:
        print("\nTo-Do List Menu :")
        print("[1] Add Task")
        print("[2] View Tasks")
        print("[3] Mark Tasks as Completed")
        print("[4] Remove Task")
        print("[5] Quit")

        choice = int(input("\nEnter your choice from 1 to 5:"))
        print('')
        
        if choice == 1:
            task = input("Enter the task: ")
            add_task(tasks, task)
            save_tasks(tasks)
            print('Message: Successfully added your task.')
        elif choice == 2:
            print('------------ Here is your tasks ------------')
            view_tasks(tasks)
            print('--------------------------------------------')
        elif choice == 3:
            view_tasks(tasks)
            idx = int(input("Enter the task index to mark as completed: ")) - 1
            complete_task(tasks, idx)
            save_tasks(tasks)
            print("Message: To-Do list is successfully updated.")
        elif choice == 4:
            view_tasks(tasks)
            idx = int(input("Enter the task index to remove: ")) - 1
            remove_task(tasks, idx)
            save_tasks(tasks)
            print("Message: Task is removed successfully.")
        elif choice == 5:
            print('Exiting....')
            break
        else:
            print('Warning: Invalid choice entered, Try again with valid choice.')

if __name__ == '__main__':
    main()