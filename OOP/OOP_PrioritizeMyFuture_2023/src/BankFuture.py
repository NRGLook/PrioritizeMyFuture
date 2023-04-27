from src.Bank import Bank
from src.ToDoListView import ToDoListView


class BankFuture(Bank):
    def __init__(self):
        super().__init__()
        self.task_for_ToDoList = ToDoListView()
        self.list_of_DONE_tasks_Future_Bank = []

    def calculate_statistic_for_task(self):
        self.list_of_DONE_tasks_Future_Bank = self.task_for_ToDoList.show_done_task()
        count_of_not_done_tasks = len(self.list_of_DONE_tasks_Future_Bank)
        print("Done task that was in your list:", count_of_not_done_tasks)
