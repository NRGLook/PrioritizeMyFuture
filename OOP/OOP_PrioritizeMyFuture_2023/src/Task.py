from var.Constants import StatusTasks
import json


class Task:
    def __init__(self):
        self.cost_name = ""
        self.name = ""
        self.status = ""
        self.category = ""
        print("Hello World")

    def set_cost_name(self, cost_name):
        self.cost_name = cost_name

    def get_cost_name(self):
        return self.cost_name

    def set_name(self, name):
        self.name = name

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

