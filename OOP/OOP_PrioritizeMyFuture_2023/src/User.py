import json
import sqlite3
import sys
import var.Constants

from passlib.hash import pbkdf2_sha256
from Bank import Bank


class User:

    def __init__(self):
        self.username = ""
        self.password = ""
        self.bank = Bank()

    def registration(self):

        print(var.Constants.GREETING_TEXT)
        conn = sqlite3.connect('users.db')
        c = conn.cursor()

        c.execute('''CREATE TABLE IF NOT EXISTS users
                     (username TEXT PRIMARY KEY, password TEXT)''')

        def verify_password(password, hashed):
            return pbkdf2_sha256.verify(password, hashed)

        username = input('Enter username: ')
        password = input('Enter password: ')
        data = {f"{username}: f[{list}]"}

        # Получаем хэш пароля из базы данных для введенного имени пользователя
        c.execute('SELECT password FROM users WHERE username=?', (username,))
        result = c.fetchone()

        # Проверяем, существует ли пользователь с таким именем в базе данных
        if result:
            # Если пользователь уже существует, проверяем введенный пароль
            if verify_password(password, result[0]):
                print('Authorization is success!')
                with open(f"{username}.json", "a") as tasks_file:
                    json.dump(self.data, tasks_file)
                user = RegisteredUser()
            else:
                print('Incorrect password! Try again!')
        else:
            # Если пользователь не существует, добавляем его в базу данных
            hashed_password = pbkdf2_sha256.hash(password)
            c.execute('INSERT INTO users VALUES (?, ?)', (username, hashed_password))
            with open(f"{username}.json", "a") as tasks_file:
                json.dump(self.data, tasks_file)
            print('Registration is success!')
            user = RegisteredUser()

        # Сохраняем изменения и закрываем соединение с базой данных
        conn.commit()
        conn.close()


class RegisteredUser(User):
    def __init__(self):
        super().__init__()
        self.response()

    def response(self):
        print(var.Constants.OPTIONS_TODO)
        while True:
            user_input = input('Choose command: ')
            if user_input == '007':
                self.show_all_tasks(self)
            if user_input == '0':
                self.show_task(self)
            if user_input == '1':
                self.add_task(self)
            if user_input == '2':
                self.remove_task(self)
            if user_input == '3':
                self.update_task(self)
            if user_input == '4':
                self.change_styles(self)
            if user_input == '5':
                self.set_name(self)
            if user_input == '6':
                self.set_y_o(self)
            if user_input == '7':
                self.get_y_o(self)
            if user_input == '8':
                self.burn_today(self)
            if user_input == '9':
                self.transfer_to_future(self)
            if user_input == '10':
                sys.exit()

    @staticmethod
    def show_all_tasks(self, bank):
        print(bank.list_of_tasks)

    @staticmethod
    def show_task(self, bank):
        operation = int(input("Enter number of task :  "))
        print(bank.list_of_tasks[operation-1])

    def add_task(self, bank):
        self.bank.set_name(input("Enter task name: "))
        self.bank.set_cost_name(int(input("Enter task cost in minutes: ")))
        self.bank.set_category(input("Enter task category: "))
        self.bank.add_list_of_tasks(self.task)

    def set_category(self, category):
        self.bank.set_category(category)
        # self.tasks.set_category(category)

    def remove_task(self, bank_today):
        operation = int(input("Enter task that are you going to remove:  "))
        self.bank_today.list_of_tasks.pop(operation-1)

    def update_task(self, bank_today):
        operation = int(input("Enter number of task that are you going to update:  "))
        choose_operation = int(input("Enter the field in task to update: \n1-name\n2-costmin\n3-category  "))
        new_parameter = input("Enter new field: ")
        self.bank_today.list_of_tasks[operation-1][choose_operation-1] = new_parameter

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

    def transfer_to_future(self):
        y_o_transfer = sum([task.cost_name for task in self.tasks])
        self.bank.change_y_o(y_o_transfer)
