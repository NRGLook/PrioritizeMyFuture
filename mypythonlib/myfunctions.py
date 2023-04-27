import json
import tomllib
import xml

"""
import var.Constants

from src.User import User, RegisteredUser
from src.RegistrationPolicy import RegistrationPolicy
from src.Bank import Bank
from src.BankFuture import BankFuture
from src.BankToday import TodayBank
from src.ItemsShop import ItemsShop
from src.Task import Task
from src.ToDoList import ToDoList
from src.ToDoListView import ToDoListView
"""

class JSON:
    def JSON_dump(self, file):
        return json.dump(self, file)

    def JSON_dumps(self):
        return json.dumps(self)

    @staticmethod
    def JSON_load(self, file):
        return json.load(file)

    @staticmethod
    def JSON_loads(self, file):
        return json.loads(file)


class TOML:

    @staticmethod
    def TOML_load(self, file):
        return tomllib.load(file)

    @staticmethod
    def TOML_loads(self, file):
        return tomllib.loads(file)


class XML:

    @staticmethod
    def XML_PARSERS(self):
        return xml.parsers
