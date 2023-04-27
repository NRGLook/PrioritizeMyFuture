from src.Bank import Bank
from src.ToDoListView import ToDoListView


class TodayBank(Bank):
    def __init__(self):
        super().__init__()
        self.task_for_ToDoList = ToDoListView()
        self.list_of_NOT_DONE_task_Today_Bank = []

    def calculate_statistic_for_task(self):
        self.list_of_NOT_DONE_task_Today_Bank = self.task_for_ToDoList.show_not_done_task()
        count_of_not_done_tasks = len(self.list_of_NOT_DONE_task_Today_Bank)
        print("Not done task that was in your list:", count_of_not_done_tasks)

