from src.Task import Task
from var.Constants import LIST_OF_ITEM_SHOP


class ItemsShop:
    def __init__(self, items=list):
        self.items = items

    def set_items(self, items):
        self.items = items

    def get_items(self):
        return self.items

    def buy_items(self):
        value_for_buy = Task.get_cost_name(self)
        print(LIST_OF_ITEM_SHOP)

