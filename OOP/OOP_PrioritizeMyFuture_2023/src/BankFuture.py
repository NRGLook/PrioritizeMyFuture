from src.Bank import Bank


class BankFuture(Bank):
    def __init__(self):
        super().__init__()
        self.list_of_not_done_tasks = []


    def calculate_interest(self):
        # реализация метода для расчета процентов для сегодняшнего банка
        pass