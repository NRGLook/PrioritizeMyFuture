import sqlite3
import sys
import datetime
from passlib.hash import pbkdf2_sha256

from mypythonlib import myfunctions

from src.BankToday import TodayBank
from src.BankFuture import BankFuture
from src.ItemsShop import ItemsShop
from src.ToDoList import ToDoList
from src.ToDoListView import ToDoListView


class User:
    def __init__(self):
        self.username = ""
        self._password = ""

    def get_username(self):
        return self.username

    def set_username(self, username):
        self.username = username

    def get_password(self):
        return self._password

    def set_password(self, _password):
        self._password = _password


class RegisteredUser(User):
    def __init__(self, username):
        super().__init__()
        self.username = username
        self.task_for_ToDoList = ToDoList()
        self.task_for_view = ToDoListView()
        self.bank_today = TodayBank()
        self.bank_future = BankFuture()
        self.minutes_left_in_day(self)
        # circle dependence -> self.bank = Bank()

    @staticmethod
    def minutes_left_in_day(self):
        now = datetime.datetime.now()
        end_of_day = now.replace(hour=23, minute=59, second=59, microsecond=999999)
        time_left = end_of_day - now
        minutes_left = int(time_left.total_seconds() // 60)
        print("Number of available (remaining) minutes per day: ", minutes_left)

    @staticmethod
    def enter_to_item_shop(self):
        ItemsShop.buy_items(self)

    def add_task(self):
        single_task = self.task_for_ToDoList.create_list()
        self.task_for_ToDoList.add_task_for_single_list(single_task)
        # print(f"Task was added to {self.username} file")
        # serialization
        # setup.DataSerializerDeserializer.JSON_dump()
        with open(f"{self.username}.json", "w") as file:
            # serialization
            myfunctions.JSON.JSON_dump(self.task_for_ToDoList.list_of_ALL_task, file)
            # json.dump(self.task_for_ToDoList.list_of_ALL_task, file)

    def remove_task(self, operation):
        self.task_for_ToDoList.remove_task(operation)
        with open(f"{self.username}.json", "w") as file:
            # serialization
            myfunctions.JSON.JSON_dump(self.task_for_ToDoList.list_of_ALL_task, file)
            # json.dump(self.task_for_ToDoList.list_of_ALL_task, file)

    def update_task(self, operation, choose_operation, new_parameter):
        operation = operation
        choose_operation = choose_operation
        new_parameter = new_parameter
        self.task_for_ToDoList.update_task(operation, choose_operation, new_parameter)
        with open(f"{self.username}.json", "w") as file:
            # serialization
            myfunctions.JSON.JSON_dump(self.task_for_ToDoList.list_of_ALL_task, file)
            # json.dump(self.task_for_ToDoList.list_of_ALL_task, file)

    def show_specific_task(self, operation):
        self.task_for_view.show_specific_task(operation)

    def show_all_tasks(self):
        with open(f"{self.username}.json", "r") as file:
            # deserialization
            all_task = myfunctions.JSON.JSON_load(self.task_for_view.list_of_ALL_task, file)
            # all_task = json.load(file)
            print(all_task)

    def show_done_task(self):
        self.task_for_view.show_done_task()

    def show_not_done_task(self):
        self.task_for_view.show_not_done_task()

    def calculate_statistic_for_not_done_task(self):
        self.bank_today.calculate_statistic_for_task()

    def calculate_statistic_for_done_task(self):
        self.bank_future.calculate_statistic_for_task()

    """
    def burn_today(self, task_for_ToDoList):
        y_o_burn = self.bank.volume - sum([task.cost_name for task in self.tasks])
        self.bank.set_y_o(self.bank.y_o + y_o_burn)
        self.bank.set_volume(1440)

    def transfer_to_future(self, task_for_ToDoList):
        y_o_transfer = sum([task.cost_name for task in self.tasks])
        self.bank.change_y_o(y_o_transfer)
    
    def add_task(self, task_for_ToDoList):
        print(f"Task was added to {self.username} file")
        single_task = self.task_for_ToDoList.create_list()
        self.task_for_ToDoList.add_task_for_single_list(single_task)
        with open(f"{self.username}.json", "r+") as file:
            try:
                data = json.load(file)
            except json.decoder.JSONDecodeError:
                data = []
            data.extend(self.task_for_ToDoList.list_of_ALL_task)
            # Deleting duplicates in task list
            data = list(set([json.dumps(i) for i in data]))
            # Write to file without duplicates
            file.seek(0)
            file.truncate()
            for task in data:
                file.write(task + "\n")
    """
