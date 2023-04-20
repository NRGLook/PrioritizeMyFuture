import json
from var.Constants import StatusTasks
from src.Bank import Bank


class Task:
    def __init__(self):
        self.name = ""
        self.cost_name = 0
        self.category = ""
        self.status = ""
        self.list_for_single_task = []

    def set_name(self, name):
        self.list_for_single_task.append(name)

    def set_cost_name(self, cost_name):
        self.list_for_single_task.append(cost_name)

    def get_cost_name(self):
        return self.cost_name

    def get_name(self):
        return self.name

    def set_status(self, status):
        self.status = status

    def change_status(self, status):
        self.status = status

    def set_category(self, category):
        self.list_for_single_task.append(category)

    def change_category(self, category):
        self.category = category

