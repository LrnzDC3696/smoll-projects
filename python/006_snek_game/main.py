from __future__ import annotations
# delays stuff so we can use Classes even if not yet defined
# see class View, class Controller
import curses
from utils import Direction, Object
from typing import Union


class Model:
    def __init__(self, y, x) -> None:
        self.y = y
        self.x = x

    def setup(self):
        self.new_dire = Direction.LEFT
        self.curr_dire = Direction.LEFT
        self.board = [
            [None for _ in range(self.x)] for _ in range(self.y)
        ]

        snake = []
        for z in range(3):
            snake.append([self.y//2, self.x//4-z])

        self.snake = snake

    @property
    def snake_head(self) -> list[int]:
        return self.snake[0]

    def process(self, key: Union[str, None]) -> None:
        dire = Direction.from_str(key)
        if dire == Direction.UNKNOWN:
            dire = self.curr_dire

        new_y = self.snake_head[0] + dire.value[0]
        new_x = self.snake_head[1] + dire.value[1]
        if self.check_if_die(new_y, new_x):
            return
        self.move_snek_to(new_y, new_x)

    def check_if_die(self, y: int, x: int) -> bool:
        obj = self.board[y][x]
        if obj in {Object.SNAKE, Object.WALL}:
            return True
        return False

    def move_snek_to(self, y: int, x: int):
        self.check_if_die(y, x)


class View:
    def setup(self, controller: Controller) -> None:
        self.controller = controller
        self.window = curses.initscr()
        self.going_brr = False
        curses.nocbreak()
        curses.echo()

    def set_window_timeout(self, n: int) -> None:
        self.window.timeout(n)

    def close_window(self) -> None:
        curses.endwin()

    def start_main_loop(self) -> None:
        """keeps waiting for input?"""
        self.set_window_timeout(75)
        self.going_brr = True
        while self.going_brr:
            self.window.move(0, 0) # moving the cursor
            try:
                key = self.window.getkey()
            except curses.error:
                key = None
            self.controller.handle_key_input(key)


class Controller:
    def __init__(self, model: Model, view: View) -> None:
        self.model = model
        self.view = view

    def start(self) -> None:
        self.view.setup(self)
        self.view.start_main_loop()

    def handle_key_input(self, key: Union[str, None]) -> None:
        self.model.process(key)


if __name__ == '__main__':
    owo = Controller(Model(75, 25), View())
    owo.start()

