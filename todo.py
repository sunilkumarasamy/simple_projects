import pandas as pd 
import numpy as np 
import os



def display_task(tasks):
	if not tasks:
		print("no tasks")
	else:
		print("Tasks:")
		for i,task in enumerate(tasks,1):
			print(f"{i}.{task}")

def add_task(tasks,new_task):
	tasks.append(new_task)
	print(f"New task {new_task} added successfully")

def remove_task(tasks, task_index):
    if 1 <= task_index <= len(tasks):
        removed_task = tasks.pop(task_index - 1)
        print(f"Task '{removed_task}' removed successfully.")
    else:
        print("Invalid task index.")


def main():
	tasks = []

	while True:
		print("/n 1. Display Task")
		print("2. Add Tasks")
		print("3. Remove Tasks")
		print("4. Quit")

		choice = input("Enter the choice 1/2/3/4: ")

		if choice == "1":
			display_task(tasks)
		elif choice =="2":
			new_task = input("Enter the task: ")
			add_task(tasks,new_task)
		elif choice =="3":
			task_index = int(input("Enter the task index to remove"))
			remove_task(tasks, task_index)
		elif choice =="4":
			print("done good bye")
			break

		else:
			print("Invalid task. Please enter the valid task")


if __name__ == "__main__":
	main()


