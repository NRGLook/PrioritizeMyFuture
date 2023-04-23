import sqlite3
import sys
import json
import datetime
import var.Constants

from passlib.hash import pbkdf2_sha256
from src.ToDoList import ToDoList
from src.ItemsShop import ItemsShop


class User:
    def __init__(self):
        self.username = ''
        self._password = ''

    def registration(self):

        print(var.Constants.GREETING_TEXT)
        conn = sqlite3.connect('users.db')
        c = conn.cursor()

        c.execute('''CREATE TABLE IF NOT EXISTS users
                     (username TEXT PRIMARY KEY, password TEXT)''')

        def verify_password(password, hashed):
            return pbkdf2_sha256.verify(password, hashed)

        self.username = input('Enter username: ')
        self._password = input('Enter password: ')

        c.execute('SELECT password FROM users WHERE username=?', (self.username,))
        result = c.fetchone()

        if result:
            if verify_password(self._password, result[0]):
                print('Authorization is success!')
                with open(f"{self.username}.json", "a") as tasks_file:
                    pass
                user = RegisteredUser(self.username)
            else:
                print('Incorrect password! Try again!')
        else:
            hashed_password = pbkdf2_sha256.hash(self._password)
            c.execute('INSERT INTO users VALUES (?, ?)', (self.username, hashed_password))
            with open(f"{self.username}.json", "a") as tasks_file:
                pass
            print('Registration is success!')
            user = RegisteredUser(self.username)

        conn.commit()
        conn.close()

    def get_username(self):
        return self.username


class RegisteredUser(User):
    def __init__(self, username):
        super().__init__()
        self.username = username
        self.task_for_ToDoList = ToDoList()
        self.minutes_left_in_day(self)
        self.response()
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
        ItemsShop.buy_items()

    def response(self):
        print(var.Constants.OPTIONS_TODO)
        while True:
            user_input = input('Choose command: ')
            if user_input == '1':
                self.add_task(self)
            if user_input == '2':
                self.remove_task(self)
            if user_input == '3':
                self.update_task(self)
            if user_input == '4':
                self.show_all_tasks(self)
            if user_input == '5':
                self.show_specific_task(self)
            if user_input == '6':
                self.show_done_task(self)
            if user_input == '7':
                self.show_not_done_task(self)
            if user_input == '8':
                self.burn_today(self)
            if user_input == '9':
                self.transfer_to_future(self)
            if user_input == '10':
                sys.exit()

    def add_task(self, task_for_ToDoList):
        single_task = self.task_for_ToDoList.create_list()
        self.task_for_ToDoList.add_task_for_single_list(single_task)
        # print(f"Task was added to {self.username} file")
        with open(f"{self.username}.json", "w") as file:
            json.dump(self.task_for_ToDoList.list_of_ALL_task, file)

    def remove_task(self, task_for_ToDoList):
        operation = int(input("Enter task that are you going to remove:  "))
        self.task_for_ToDoList.remove_task(operation)
        with open(f"{self.username}.json", "w") as file:
            json.dump(self.task_for_ToDoList.list_of_ALL_task, file)

    def update_task(self, task_for_ToDoList):
        operation = int(input("Enter number of task that are you going to update:  "))
        choose_operation = int(input("Enter the field in task to update:\n1-name\n2-cost\n3-category\n"))
        new_parameter = input("Enter new field: ")
        self.task_for_ToDoList.update_task(operation, choose_operation, new_parameter)
        with open(f"{self.username}.json", "w") as file:
            json.dump(self.task_for_ToDoList.list_of_ALL_task, file)

    def show_specific_task(self, task_for_ToDoList):
        operation = int(input("Enter number of task: "))
        self.task_for_ToDoList.show_specific_task(operation)

    def show_all_tasks(self, task_for_ToDoList):
        with open(f"{self.username}.json", "r") as file:
            all_task = json.load(file)
            print(all_task)

    def show_done_task(self, task_for_ToDoList):
        self.task_for_ToDoList.show_done_task(self.task_for_ToDoList)

    def show_not_done_task(self, task_for_ToDoList):
        self.task_for_ToDoList.show_not_done_task(self.task_for_ToDoList)

    def burn_today(self, task_for_ToDoList):
        y_o_burn = self.bank.volume - sum([task.cost_name for task in self.tasks])
        self.bank.set_y_o(self.bank.y_o + y_o_burn)
        self.bank.set_volume(1440)

    def transfer_to_future(self, task_for_ToDoList):
        y_o_transfer = sum([task.cost_name for task in self.tasks])
        self.bank.change_y_o(y_o_transfer)

    """
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
            # Удаление дубликатов в списке задач
            data = list(set([json.dumps(i) for i in data]))
            # Запись списка задач без дубликатов в файл
            file.seek(0)
            file.truncate()
            for task in data:
                file.write(task + "\n")
    """
