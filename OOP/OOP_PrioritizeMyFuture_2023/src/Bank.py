import json

from abc import ABC, abstractmethod
from src.ToDoList import ToDoList


class Bank(ABC):
    def __init__(self):
        self.styles = None
        self.volume = 1440
        self.to_do_list = ToDoList()

    @property
    def style(self):
        return self.styles

    @style.setter
    def style(self, styles):
        self.styles = styles

    @abstractmethod
    def calculate_statistic_for_task(self):
        pass

    @staticmethod
    def get_list_of_ALL_tasks(self):
        with open(f"{self.get_username}", "r") as file:
            json.load(file)
            file.write("\n")
