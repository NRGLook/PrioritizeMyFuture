import json
from abc import ABC, abstractmethod


class Bank(ABC):
    def __init__(self):
        self.volume = 1440
        self.name = ""
        self.list_of_tasks = {[{}, {}, {}], ...}

    def add_list_of_tasks(self, task):
        print("Hello its add method")
        self.list_of_tasks.append(task)
        with open("ilya.json", "w") as file:
            json.dump(self.list_of_tasks, file)

    def set_volume(self, volume):
        self.volume = volume

    def set_styles(self, styles):
        self.styles = styles

    def change_styles(self, styles):
        self.styles += styles

    def set_name(self, name):
        self.name = name

    def set_y_o(self, y_o):
        self.y_o = y_o

    def change_y_o(self, y_o):
        self.y_o += y_o

    def get_y_o(self):
        return self.y_o

    @abstractmethod
    def calculate_interest(self):
        pass