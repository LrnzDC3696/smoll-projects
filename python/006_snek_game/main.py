from __future__ import annotations
import curses
from utils import Direction, Status, Object, add_list
from typing import Union, Any


class Model:
    def setup(self, y: int, x: int) -> None:
        self.y = y
        self.x = x
        self.new_dire = Direction.LEFT
        self.curr_dire = Direction.LEFT
        self.board = [
            [None for _ in range(self.x)] for _ in range(self.y)
        ]

        snake = []
        for z in range(3):
            snake.append([self.y//2, self.x//4-z])

        self.snake = snake

    def move(self) -> None:
        new_y, new_x = add_list(self.snake_head, self.curr_dire.value)

    def change_direction(self, direction: Direction):
        if direction == Direction.UNKNOWN:
            direction = self.curr_dire
        else:
            direction = self.new_dire

    @property
    def snake_head(self) -> tuple[int, int]:
        y, x = self.snake[0]
        return y, x

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
        self.view.setup(self)
        self.start_gaeming()
        self.view.close_window()

    def start_gaeming(self) -> Status:
        running = True
        temporary_counter = 0

        while running:
            key = self.view.wait_for_input()

            if key == 'q':
                running = False
                return Status.QUIT

            direction = Direction.from_str(key)

            self.model.change_direction(direction)
            is_ded = self.model.check_if_die(
                *add_list(self.model.snake_head, self.model.curr_dire.value)
            )

            if is_ded:
                running = False
                return Status.DEAD

            # ----------
            temporary_counter += 1
            if temporary_counter <= 1000:
                break

        return Status.QUIT


if __name__ == '__main__':
    ctrl = Controller(Model(), View())
    ctrl.start()
