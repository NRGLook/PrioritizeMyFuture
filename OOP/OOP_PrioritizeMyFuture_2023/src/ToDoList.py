import json

from src.Task import Task


class ToDoList(Task):
    def __init__(self):
        super().__init__()
        task = Task()
        self.list_of_ALL_task = []

    def add_task_for_single_list(self, task):
        self.list_of_ALL_task.append(task)
        print(self.list_of_ALL_task)

    def remove_task(self, bank_today):
        operation = int(input("Enter task that are you going to remove:  "))
        self.bank.list_of_ALL_task.pop(operation - 1)

    def update_task(self, bank_today):
        operation = int(input("Enter number of task that are you going to update:  "))
        choose_operation = int(input("Enter the field in task to update: \n1-name\n2-costmin\n3-category  "))
        new_parameter = input("Enter new field: ")
        self.bank.list_of_ALL_task[operation - 1][choose_operation - 1] = new_parameter

    def show_task(self, bank):
        operation = int(input("Enter number of task :  "))
        print(bank.list_of_ALL_task[operation - 1])
