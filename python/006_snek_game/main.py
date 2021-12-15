"""
events mvc

y, x in a cartesian plane
"""

import random
from enum import Enum
import curses
from curses import wrapper


class Object(Enum):
    WALL  = '#'
    SPACE = ' '
    FOOD  = '@'
    SNAKE = 'O'


class Board:
    def __init__(self, y=75, x=20):
        y -= 1
        x -= 1
        self.y = y
        self.x = x
        self.board = [[Object.SPACE for _ in range(x)] for _ in range(y)]
        self.snake = []

        # set stuff up
        self.setup_wall()
        self.put_snake()
        self.put_food()

    def put_snake(self, y=None, x=None):
        """Tries to put the snek in the middle"""
        y = y if y is not None else int(self.y/2)
        x = x if x is not None else int(self.x/4)
        for z in range(3):
            # snake[0][0] is the head
            self.snake.append([y, x-z])
            self.board[y][x-z] = Object.SNAKE

    def put_food(self):
        """Tries to put a food in a location
        if the food can't find a place for 1000th time if returns False
        """
        loop_counter = 0
        while True:
            if loop_counter >= 1000:
                return None, None

            y = random.randint(1, self.y-2)
            x = random.randint(1, self.x-2)
            if self.board[y][x] != Object.SPACE:
                continue
            self.board[y][x] = Object.FOOD
            break

        return y,x


    def setup_wall(self):
        """Sets up the wall of the board"""
        for y in range(self.y):

            if y in (0, self.y-1):
                for x in range(self.x):
                    self.board[y][x] = Object.WALL
                continue

            for x in {0, self.x-1}:
                self.board[y][x] = Object.WALL


    def __str__(self):
        return '\n'.join(
            [''.join([obj.value for obj in y]) for y in self.board]
        )

direction = {
    'k': (-1, 0),
    'j': (1, 0),
    'h': (0, -1),
    'l': (0, 1),
}

opposites = (['k', 'j'],['j', 'k'], ['h', 'l'], ['l', 'h'])


# should add a thing so when I go to the opposite direction I can still go brr
def start_gaeming(screen, board):
    key = 'l'
    screen.timeout(100)
    screen.clear()
    screen.addstr(0, 0, str(board))

    while True:
        screen.move(0,0)
        # make this thing better this is definetely gay
        screen.refresh()

        try:
            next_key = screen.getkey()
        except:
            next_key = key

        if [key, next_key] in opposites:
            key = key
        elif direction.get(next_key) is not None:
            key = next_key
        elif direction.get(next_key) == -1:
            key = next_key
        elif next_key == 'q':
            break

        move_to = direction[key]

        # check if dead
        cur_y, cur_x = board.snake[0]
        new_y, new_x = (cur_y+move_to[0], cur_x+move_to[1])

        if board.board[new_y][new_x] in (Object.WALL, Object.SNAKE):
            screen.nodelay(False)
            screen.clear()
            screen.addstr('You died')
            screen.getkey()
            screen.refresh()
            break

        if board.board[new_y][new_x] == Object.FOOD:
            y, x = board.put_food()
            screen.addstr(y, x, Object.FOOD.value)
        else:
            tail_y, tail_x = board.snake.pop()
            board.board[tail_y][tail_x] = Object.SPACE
            screen.addstr(tail_y, tail_x, Object.SPACE.value)
            board.board[new_y][new_x] = Object.SNAKE
            screen.addstr(new_y, new_x, Object.SNAKE.value)


        board.snake.insert(0, [new_y, new_x])



def main(screen):
    is_gaeming = True

    while is_gaeming:
        start_gaeming(screen, board = Board(*screen.getmaxyx()))
        screen.addstr(0, 0, 'wanna play again? y/n')
        while True:
            owo = screen.getkey()
            if owo in {'y', 'n'}:
                break
        if owo == 'n':
            break


if __name__ == '__main__':
    wrapper(main)
