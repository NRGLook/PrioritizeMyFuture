from enum import Enum


class StatusTasks(Enum):
    DONE = 1
    PENDING = 0


class CategoryTasks(Enum):
    NONE = 0
    DOING = 0.5
    CUSTOM = 0.1
