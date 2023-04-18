from enum import Enum

OPTIONS_TODO = """1 - add task(description of the task)
2 - remove task
3 - update task
4 - change styles
5 - set hashtag of the task
6 - set y.o. for your task
7 - get y.o. for the task
8 - burn today 
9 - transfer_to_future
10 - exit"""



OPTIONS_EDIT_TASK = """0 - response
\n1 - remove task
\n2 - change to DONE
\n3 - update"""

OPTIONS_UPDATE = """0 - response
\n1 - edit name
\n2 - edit category"""


class StatusTasks(Enum):
    DONE = 1
    PENDING = 0


class CategoryTasks(Enum):
    NONE = 0
    DOING = 0.5
    CUSTOM = 0.1
