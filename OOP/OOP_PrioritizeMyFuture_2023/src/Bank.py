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
        print(len(self.to_do_list.list_of_ALL_task))

