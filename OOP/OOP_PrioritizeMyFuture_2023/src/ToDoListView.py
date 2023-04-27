from src.ToDoList import ToDoList


class ToDoListView(ToDoList):

    def show_specific_task(self, operation):
        print("Task what you choose: ", self.list_of_ALL_task[operation - 1])

    def show_not_done_task(self):
        for task in self.list_of_ALL_task:
            if task[3] == "Not Done":
                print(task[0], "is", task[3])
                self.list_of_NOTDONE_task.append(list)
        if len(self.list_of_NOTDONE_task) == 0:
            print("There is no NOT DONE tasks yet!")
        return self.list_of_NOTDONE_task

    def show_done_task(self):
        for task in self.list_of_ALL_task:
            if task[3] == "Done":
                print(task[0], "is", task[3])
                self.list_of_DONE_task.append(list)
        if len(self.list_of_DONE_task) == 0:
            print("There is no DONE tasks yet!")
        return self.list_of_DONE_task
