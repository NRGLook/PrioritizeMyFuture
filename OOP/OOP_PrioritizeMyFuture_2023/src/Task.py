import datetime


class Task:
    def __init__(self):
        self.name = ""
        self.category = ""
        self.cost_name = 0
        self.status = "Not Done"
        self.available_minutes = 0

    def set_name(self):
        self.name = input("Enter task name: ")
        return self.name

    def set_cost_name(self):
        self.cost_name = int(input("Enter task cost in minutes: "))
        now = datetime.datetime.now()
        end_of_day = now.replace(hour=23, minute=59, second=59, microsecond=999999)
        time_left = end_of_day - now
        minutes_left = int(time_left.total_seconds() // 60)
        self.available_minutes = minutes_left - self.cost_name
        if self.available_minutes <= 0:
            print("Incorrect value! Please, try to add task again!")
            return "0"
        print("Number of available (remaining) minutes per day: ", self.available_minutes-self.cost_name)
        return self.cost_name

    def get_available_minutes(self):
        return self.available_minutes

    def get_cost_name(self):
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

