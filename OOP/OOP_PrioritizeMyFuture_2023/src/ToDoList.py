import json

from src.Task import Task


class ToDoList(Task):
    def __init__(self):
        super().__init__()
        task = Task()
        self.list_of_ALL_task = []

    def add_task_for_single_list(self, task):
        self.list_of_ALL_task.append(task)
        print("Task was added: ", self.list_of_ALL_task)

    def remove_task(self, operation):
        self.list_of_ALL_task.pop(operation - 1)
        print("Task was deleted: ", self.list_of_ALL_task)

    def update_task(self, operation, choose_operation, new_parameter):
        self.list_of_ALL_task[operation - 1][choose_operation - 1] = new_parameter
        print("Task was updated: ", self.list_of_ALL_task)

    def show_specific_task(self, operation):
        print("Task what you choose: ", self.list_of_ALL_task[operation - 1])
