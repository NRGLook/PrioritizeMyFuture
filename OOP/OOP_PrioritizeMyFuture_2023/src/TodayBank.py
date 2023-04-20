from src.Bank import Bank
from src.Task import Task
import json


class TodayBank(Bank):
    def __init__(self):
        super().__init__()
        task = Task()
        self.list_of_tasks = []

    def add_list_of_tasks(self, task):
        self.list_of_tasks.append(task.dict_for_task)
        with open("ilya.json", "w") as file:
            file.write(json.dumps(self.list_of_tasks))
        print("Task was added")
        print(self.list_of_tasks)

    def calculate_interest(self):
        # реализация метода для расчета процентов для сегодняшнего банка
        pass