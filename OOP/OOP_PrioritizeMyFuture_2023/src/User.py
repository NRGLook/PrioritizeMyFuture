import var.Constants
from src.Task import Task


class User:
    def __init__(self):
        self.username = ""
        self.password = ""
        self.login_status = False

    def registration(self):
        self.username = input("Enter username: ")
        self.password = input("Enter password: ")

    def login(self, username, password):
        if self.username == username and self.password == password:
            self.login_status = True
            return True
        else:
            return False


