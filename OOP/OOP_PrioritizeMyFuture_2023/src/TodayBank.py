import json
from abc import ABC

from src.Bank import Bank


class TodayBank(Bank, ABC):
    def __init__(self):
        super().__init__()
        self.list_of_NOT_DONE_tasks = []

    def calculate_statistic_for_task(self):
        pass

"""
    def add_list_of_tasks(self, task):
        with open(f"{User.username}.json", "a") as file:
            json.dump(task.create_list(), file)
            file.write("\n")
        print("Task was added")
        self.list_of_tasks.append(task.create_list())
        print(self.list_of_tasks)

    def calculate_statistic_for_task(self):
        pass
"""
