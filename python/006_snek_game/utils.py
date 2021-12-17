from enum import Enum

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
