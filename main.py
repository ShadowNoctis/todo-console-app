import os
import time

tasks = []
cursor = ">"

def add_task(task):
    pass

def remove_task(task):
    pass

def display_tasks():
    pass

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
        pass
    elif (int(chosen) == 2):
        pass
    elif (int(chosen) == 3):
        pass
    elif (int(chosen) == 4):
        quit_app()
    else:
        clear_screen()
        print("Enter A Valid Number")
        time.sleep(0.5)
        clear_screen()