from abc import ABC
from src.Bank import Bank
from src.ToDoList import ToDoList
from src.Task import Task


class TodayBank(Bank, ABC):
    def __init__(self):
        super().__init__()
        self.task = Task()
        self.task_for_ToDoList = ToDoList()
        self.list_of_NOT_DONE_task_Today_Bank = []

    def calculate_statistic_for_task(self):
        self.list_of_NOT_DONE_task_Today_Bank = self.task_for_ToDoList.get_list_of_NOTDONE_task()
        count_of_not_done_tasks = len(self.list_of_NOT_DONE_task_Today_Bank)
        print(count_of_not_done_tasks)

