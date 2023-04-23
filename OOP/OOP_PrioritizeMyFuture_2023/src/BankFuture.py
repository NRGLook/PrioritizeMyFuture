from abc import ABC

from src.Bank import Bank


class BankFuture(Bank, ABC):
    def __init__(self):
        super().__init__()
        self.list_of_DONE_tasks = []

    def calculate_statistic_for_task(self):
        count_of_done_tasks = 0
        while True:
            if self.to_do_list.list_of_ALL_task[4] == "Done":
                count_of_done_tasks += 1
            else:
                break
        print(count_of_done_tasks)
