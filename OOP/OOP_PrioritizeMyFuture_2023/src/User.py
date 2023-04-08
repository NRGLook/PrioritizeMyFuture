import var.Constants
from src.Task import Task
from var.Constants import StatusTasks
class User:
    def __init__(self):
        self.name = input("Enter your username: ")
        self.__password = input("Enter your password: ")

    def registration(self):
        pass


class RegistrationUser(User):
    def __int__(self):
        self.lists_of_tasks = []
        self.task = Task

    def add_task(self, task):
        self.lists_of_tasks.append(task)

    def remove_task(self, task):
        self.lists_of_tasks.remove(task)

    def update_task(self, task, position, new_task):
        self.lists_of_tasks[position] = self.lists_of_tasks[new_task]

    def change_styles(self, status=var.Constants.StatusTasks):
        self.task.change_status(status)


