import datetime


class Task:
    def __init__(self):
        self.name = ""
        self.category = ""
        self.cost_name = 0
        self.status = "Not Done"

    """
    @property
    def name(self):
        return self.name

    @property
    def cost_name(self):
        return self.cost_name

    @property
    def category(self):
        return self.category

    @property
    def status(self):
        return self.status
    """
    def set_name(self):
        self.name = input("Enter task name: ")
        return self.name

    def set_cost_name(self):
        self.cost_name = int(input("Enter task cost in minutes: "))
        return self.cost_name

    def set_category(self):
        self.category = input("Enter task category: ")
        return self.category

    def set_status(self):
        return self.status

    def create_list(self):
        list_for_single_task = []
        list_for_single_task.append(self.set_name())
        list_for_single_task.append(self.set_cost_name())
        list_for_single_task.append(self.set_category())
        list_for_single_task.append(self.set_status())
        return list_for_single_task

