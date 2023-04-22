import json

from abc import ABC, abstractmethod
from src.User import User
from src.Task import Task


class Bank(ABC):
    def __init__(self):
        self.styles = None
        self.volume = 1440
        self.name = ""
        self.list_of_all_tasks = []
        task = Task()

    @staticmethod
    def get_list_of_all_tasks(self):
        with open(f"{User.username}.json", "r") as file:
            json.load(self.list_of_all_tasks, file)
            file.write("\n")

    @property
    def style(self, styles):
        self.styles += styles

    @style.setter
    def style(self, styles):
        self.styles = styles

    @abstractmethod
    def calculate_statistic_for_task(self):
        pass
