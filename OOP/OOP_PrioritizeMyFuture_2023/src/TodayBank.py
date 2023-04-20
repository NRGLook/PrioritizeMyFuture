from src.Bank import Bank
from src.Task import Task
import json


class TodayBank(Bank):
    def __init__(self):
        super().__init__()
        task = Task()

    def add_list_of_tasks(self, task):
        with open("ilya.json", "a") as file:
            json.dump(task.dict_for_task, file)
        print("Task was added")
        task.list_of_tasks.append(task.dict_for_task)
        print(task.list_of_tasks)

    def calculate_interest(self):
        # реализация метода для расчета процентов для сегодняшнего банка
        pass