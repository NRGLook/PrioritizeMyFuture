import json
from var.Constants import StatusTasks
from src.Bank import Bank


class Task:
    def __init__(self, cost_name):
        self.name = ""
        self.cost_name = cost_name
        self.category = ""
        self.status = ""

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

