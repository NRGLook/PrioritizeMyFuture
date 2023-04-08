from var.Constants import StatusTasks


class Task:
    def __int__(self, cost_time, name, teg, status, category):
        self.cost_time = cost_time
        self.name = name
        self.teg = teg
        self.status = StatusTasks
        self.category = category

    def set_cost_time(self):
        pass

    def get_cost_time(self):
        pass

    def set_name(self):
        pass

    def get_name(self):
        pass

    def set_status(self):
        pass

    def change_status(self):
        pass

    def set_category(self):
        pass

    def change_category(self):
        pass
