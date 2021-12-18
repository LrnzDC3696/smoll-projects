from enum import Enum, auto
from typing import Union

def add_list(list1: Union[list, tuple], list2: Union[list, tuple]) -> tuple[int, int]:
    return (list1[0] + list2[0], list1[1] + list2[1])

class Status(Enum):
    DEAD = auto()
    MOVED = auto()
    GAEMING = auto()
    QUIT = auto()

class Object(Enum):
    SNAKE_HEAD = '@'
    SNAKE_BODY = 'O'
    SNAKE = 'O'
    SPACE = ' '
    APPLE = '*'
    WALL = '#'

class Direction(Enum):
    UP = (-1, 0)
    DOWN = (1, 0)
    LEFT = (0, -1)
    RIGHT = (0, 1)
    UNKNOWN = None

    @classmethod
    def from_str(cls, string):
        if string == 'k':
            return cls.UP
        elif string == 'j':
            return cls.DOWN
        elif string == 'h':
            return cls.LEFT
        elif string == 'l':
            return cls.RIGHT
        else:
            return cls.UNKNOWN
