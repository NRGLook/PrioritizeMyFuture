from src.Task import Task


class ToDoList(Task):
    def __init__(self):
        super().__init__()
        task = Task()
        self.list_of_ALL_task = []
        self.list_of_DONE_task = []
        self.list_of_NOTDONE_task = []

    def add_task_for_single_list(self, task):
        self.list_of_ALL_task.append(task)
        print("Task was added: ", self.list_of_ALL_task)

    def remove_task(self, operation):
        self.list_of_ALL_task.pop(operation - 1)
        print("Task was deleted: ", self.list_of_ALL_task)
        print("Now you have", Task.get_available_minutes)

    def update_task(self, operation, choose_operation, new_parameter):
        self.list_of_ALL_task[operation - 1][choose_operation - 1] = new_parameter
        print("Task was updated: ", self.list_of_ALL_task)

    def show_specific_task(self, operation):
        print("Task what you choose: ", self.list_of_ALL_task[operation - 1])

    def show_done_task(self, task_for_ToDoList):
        list = [Task.create_list(task_for_ToDoList)]
        for list in self.list_of_ALL_task:
            if list[3] == "Not Done":
                print(list[0], "is", list[3])
        """
        iterable_value = len(self.list_of_ALL_task) - 1
        help_value = 0
        hello = 0
        for iterable_value, self.status in self.list_of_ALL_task:
            if self.list_of_ALL_task[help_value][3] == "Done":
                hello += 1
            help_value += 1
        while True:
            if self.list_of_ALL_task[help_value][3] == "Done":
                self.list_of_DONE_task.append(task_for_ToDoList)
                print(self.list_of_DONE_task)
            else:
                print("There is no tasks")
                break
        """

    def show_not_done_task(self, task_for_ToDoList):
        while True:
            if self.list_of_ALL_task[3] == "Not Done":
                self.list_of_DONE_task.append(task_for_ToDoList)
                print(self.list_of_NOTDONE_task)
            else:
                print("There is no tasks")
                break
