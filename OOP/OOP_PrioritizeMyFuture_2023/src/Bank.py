import json
from abc import ABC, abstractmethod
from src.User import User
from src.Task import Task


class Bank(ABC):
    def __init__(self):
        self.volume = 1440
        self.name = ""
        self.list_of_tasks = []
        task = Task()

    def get_list_of_tasks(self):
        list_of_ALL_task = []
        with open(f"{User.username}.json", "r") as file:
            json.load(list_of_ALL_task, file)
            file.write("\n")

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
