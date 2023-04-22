from abc import ABC

from src.Bank import Bank


class BankFuture(Bank, ABC):
    def __init__(self):
        super().__init__()
        self.list_of_DONE_tasks = []

    def calculate_statistic_for_task(self):
        pass
