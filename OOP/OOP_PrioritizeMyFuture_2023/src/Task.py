import json

from src.User import User


class Task:
    def __init__(self):
        self.name = ""
        self.cost_name = 0
        self.category = ""
        self.status = ""
        self.list_of_tasks = []

    def add_list_of_tasks(self, task):
        with open(f"{User.get_username()}.json", "a") as file:
            json.dump(task.create_list(), file)
            file.write("\n")
        print("Task was added")
        self.list_of_tasks.append(task.create_list())
        print(self.list_of_tasks)

    def set_name(self, name):
        self.name = name

    def set_cost_name(self, cost_name):
        self.cost_name = cost_name

    def get_cost_name(self):
        return self.cost_name

    def get_name(self):
        return self.name

    def set_status(self, status):
        self.status = status

    def change_status(self, status):
        self.status = status

    def set_category(self, category):
        self.category = category

    def change_category(self, category):
        self.category = category

    def get_category(self):
        return self.category

    def create_list(self):
        list_for_single_task = []
        list_for_single_task.append(self.get_name())
        list_for_single_task.append(self.get_cost_name())
        list_for_single_task.append(self.get_category())
        return list_for_single_task


