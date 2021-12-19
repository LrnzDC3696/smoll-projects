from __future__ import annotations
import curses
import random
from utils import Direction, Status, Object, add_list
from typing import Union


class Model:
    def setup(self, y: int, x: int) -> None:
        self.y = y
        self.x = x
        self.new_dire = Direction.LEFT
        self.curr_dire = Direction.LEFT
        self.board = [
            [Object.SPACE for _ in range(self.x)] for _ in range(self.y)
        ]

        self.setup_snake()

    def setup_snake(self) -> None:
        snake = []

        for z in range(3):
            new_y, new_x = self.y//2, self.x//4-z
            snake.append([new_y, new_x])
            self.board[new_y][new_y] = Object.SNAKE

        self.snake = snake

    def change_direction(self, direction: Direction) -> None:
        if direction == Direction.UNKNOWN:
            direction = self.curr_dire
        else:
            direction = self.new_dire

    def generate_food(self) -> tuple[bool, int, int]:
        status = 0
        while status <= 1000:
            status += 1

            y = random.randint(1, self.y-2)
            x = random.randint(1, self.x-2)
            if self.board[y][x] != Object.SPACE:
                continue
            self.board[y][x] = Object.APPLE
            break
        else:
            return False, 0, 0
        return True, y, x

    @property
    def snake_head(self) -> tuple[int, int]:
        y, x = self.snake[0]
        return y, x

    def move_snek(self) -> tuple[Status, int, int]:
        new_y, new_x = add_list(self.snake_head, self.curr_dire.value)
        obj = self.board[new_y][new_x]

        if obj in {Object.WALL, Object.SNAKE}:
            return Status.DEAD, 0, 0
        elif obj == Object.APPLE:
            self.board[new_y][new_x] = Object.SNAKE
            return Status.EAT, new_y, new_x

        self.board[new_y][new_x] = Object.SNAKE
        return Status.MOVED, new_y, new_x


class View:
    def setup(self, controller: Controller) -> None:
        self.controller = controller
        self.window = curses.initscr()
        self.going_brr = False
        curses.nocbreak()
        curses.echo()

        self.set_window_timeout(75)

    def set_window_timeout(self, n: int) -> None:
        self.window.timeout(n)

    def close_window(self) -> None:
        curses.endwin()

    def update_str_at(self, y, x, string) -> None:
        self.window.addstr(y, x, string)

    def wait_for_input(self) -> Union[None, str]:
        try:
            self.window.getkey()
        except:
            return None


class Controller:
    def __init__(self, model: Model, view: View) -> None:
        self.model = model
        self.view = view

    def start(self) -> None:
        self.model.setup(75, 20)
        self.view.setup(self)

        self.start_gaeming()
        self.view.close_window()

    def start_gaeming(self) -> Status:
        temporary_counter = 0

        while True:
            key = self.view.wait_for_input()
            if key == 'q':
                return Status.QUIT

            direction = Direction.from_str(key)

            self.model.change_direction(direction)
            status, y, x = self.model.move_snek()

            # move the snake
            # self.model.move_snek_to()
            # move the tail

            # ----------
            temporary_counter += 1
            if temporary_counter <= 1000:
                return Status.QUIT



if __name__ == '__main__':
    ctrl = Controller(Model(), View())
    ctrl.start()
