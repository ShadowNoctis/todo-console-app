import os
import time

tasks = []
cursor = ">"

def add_task(task):
    tasks.append(task)
    clear_screen()
    input("Task Added Successfully! Press Any Key To Go Back.")

def remove_task(task):
    for taskInArray in tasks:
        if taskInArray == task:
            tasks.remove(task)
            clear_screen()
            input("Task Removed Successfully! Press Any Key To Go Back.")
            clear_screen()
        else:
            clear_screen()
            input("No Task Found. Press Any Key To Go Back.")
            clear_screen()

def display_tasks():
    for task in tasks:
        print(task)

def quit_app():
    quit()

def clear_screen():
    os.system("cls")

while True:
    print("Welcome To Your Very Own Personal Todo App!")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. View Tasks")
    print("4. Quit")
    chosen = input("Please Select What You Would Like To Do Next (Enter A Numerical Value) " + cursor + " ")

    if (int(chosen) == 1):
        clear_screen()
        user_task = input("Enter A Task: " + cursor + " ")
        add_task(user_task)
        clear_screen()
    elif (int(chosen) == 2):
        clear_screen()
        user_task_remove = input("Which task to remove " + cursor + " ")
        remove_task(user_task_remove)
    elif (int(chosen) == 3):
        clear_screen()
        display_tasks()
        input("\nPress Any Key To Go Back")
        clear_screen()
    elif (int(chosen) == 4):
        quit_app()
    else:
        clear_screen()
        print("Enter A Valid Number")
        time.sleep(0.5)
        clear_screen()