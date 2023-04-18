import var.Constants
import sqlite3
from passlib.hash import pbkdf2_sha256
from src.RegisteredUser import RegisteredUser


class User:
    def __init__(self):
        self.username = ""
        self.password = ""
        self.login_status = False
        # Подключаемся к базе данных
        conn = sqlite3.connect('users.db')
        c = conn.cursor()

        # Создаем таблицу пользователей, если ее еще нет
        c.execute('''CREATE TABLE IF NOT EXISTS users
                     (username TEXT PRIMARY KEY, password TEXT)''')

        # Функция для проверки введенного пароля
        def verify_password(password, hashed):
            return pbkdf2_sha256.verify(password, hashed)

        # Запрос у пользователя логина и пароля
        username = input('Введите имя пользователя: ')
        password = input('Введите пароль: ')

        # Получаем хэш пароля из базы данных для введенного имени пользователя
        c.execute('SELECT password FROM users WHERE username=?', (username,))
        result = c.fetchone()

        # Проверяем, существует ли пользователь с таким именем в базе данных
        if result:
            # Если пользователь уже существует, проверяем введенный пароль
            if verify_password(password, result[0]):
                print('Авторизация прошла успешно!')
                new_user = RegisteredUser()
            else:
                print('Неправильный пароль')
        else:
            # Если пользователь не существует, добавляем его в базу данных
            hashed_password = pbkdf2_sha256.hash(password)
            c.execute('INSERT INTO users VALUES (?, ?)', (username, hashed_password))
            print('Регистрация прошла успешно!')
            new_user = RegisteredUser()

        # Сохраняем изменения и закрываем соединение с базой данных
        conn.commit()
        conn.close()

"""
    def registration(self):
        self.username = input("Enter username: ")
        self.password = input("Enter password: ")

    def login(self, username, password):
        if self.username == username and self.password == password:
            self.login_status = True
            return True
        else:
            return False
"""

