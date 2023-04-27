from src.Task import Task


class ToDoList(Task):

    list_of_ALL_task = []
    list_of_DONE_task = []
    list_of_NOTDONE_task = []

    def __init__(self):
        super().__init__()
        task = Task()

    def add_task_for_single_list(self, task):
        self.list_of_ALL_task.append(task)
        print("Task was added: ", self.list_of_ALL_task)

    def remove_task(self, operation):
        self.list_of_ALL_task.pop(operation - 1)
        print("Task was deleted: ", self.list_of_ALL_task)

    def update_task(self, operation, choose_operation, new_parameter):
        self.list_of_ALL_task[operation - 1][choose_operation - 1] = new_parameter
        print("Task was updated: ", self.list_of_ALL_task)

    def set_list_of_ALL_task(self, list_of_ALL_task):
        self.list_of_ALL_task = list_of_ALL_task

    def get_list_of_ALL_task(self):
        return self.list_of_ALL_task

    def set_list_of_DONE_task(self, list_of_DONE_task):
        self.list_of_DONE_task = list_of_DONE_task

    def get_list_of_DONE_task(self):
        return self.list_of_DONE_task

    def set_list_of_NOTDONE_task(self, list_of_NOTDONE_task):
        self.list_of_NOTDONE_task = list_of_NOTDONE_task

    def get_list_of_NOTDONE_task(self):
        return self.list_of_NOTDONE_task
