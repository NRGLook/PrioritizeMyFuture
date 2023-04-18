from TodayBank import TodayBank
from User import User


class RegisteredUser(User):
    def __init__(self):
        super().__init__()
        self.tasks = []
        self.bank = TodayBank()
        print("Hello World - new user!")

    def add_task(self, task):
        task.set_name(input("Enter task name: "))
        task.set_cost_name(int(input("Enter task cost in minutes: ")))
        task.set_category(input("Enter task category: "))
        self.tasks.append(task)

    def remove_task(self, task):
        task.set_name(input("Enter task that are you going to remove:  "))
        self.tasks.remove(task)

    def update_task(self, task, new_task):
        index = self.tasks.index(task)
        self.tasks[index] = new_task

    def change_styles(self, styles):
        self.bank.change_styles(styles)

    def set_name(self, name):
        self.bank.set_name(name)

    def set_y_o(self, y_o):
        self.bank.set_y_o(y_o)

    def get_y_o(self):
        return self.bank.get_y_o()

    def burn_today(self):
        y_o_burn = self.bank.volume - sum([task.cost_name for task in self.tasks])
        self.bank.set_y_o(self.bank.y_o + y_o_burn)
        self.bank.set_volume(1440)
        self.tasks = []

    def transfer_to_future(self):
        y_o_transfer = sum([task.cost_name for task in self.tasks])
        self.bank.change_y_o(y_o_transfer)
        self.tasks = []
