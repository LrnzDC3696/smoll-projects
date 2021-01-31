"""My own tic tac toe 1.0"""

import random
import os
from time import sleep

def clear(last_words='', time=0, stop=True):
    """clears the console"""
    print(last_words)
    if stop:
        input()
    sleep(time)
    os.system('clear')

GAME_BOARD = {
    'board':"""
  1  |  2  |  3  
  4  |  5  |  6  
  7  |  8  |  9  
""",
    'data' :[[],[],[],[],[],[],[],[],[]],
    'user_turn' :True
    }

def main_menu(board_dict: dict):
    username = input('Please type your name: ')
    print(f'\nWelcome {username} you will be playing against a bot')
    clear('Press Enter to Play')
    take_turns(board_dict)
    
def take_turns(board_dict):
    if board_dict['user_turn']:
        print('Pick a number to place your piece')
    else:
        print('Bot is choose a number to place your piece')
    
    print(board_dict['board'])
    while True:
        try:
            if board_dict['user_turn']:
                choice = int(input('Your choice: '))
            else:
                choice = random.randint(0,9)
                
            if board_dict['data'][int(choice)-1]:
                print('sorry that place is taken try again')
                continue

        except ValueError:
            print('sorry input is invalid try again')
        
        except IndexError:
            print('sorry that number is invalid')
        
        else:
            break
    update_board(board_dict, choice, board_dict['user_turn'])

def update_board(board_dict, choice, turn_by_user):
    board_dict['data'][choice -1] = 1 if turn_by_user else 2
    board_dict['board'] = board_dict['board'].replace(str(choice), 'X' if turn_by_user else 'O')
    game_check(board_dict)
    
def game_check(board_dict):
    
    temporary_list = board_dict['data']
    checking = True
    to_find = 1 if board_dict['user_turn'] else 2
    
    while checking:
        """horizontal check"""
        for layer in 0,3,6:
            temp = 0
            
            for row in range(layer, layer+3):
                
                if board_dict['data'][row] == to_find: temp += 1
                if temp == 3:
                    clear('CONGRATS')
                    
        """diagonal check"""
        for layer in 0,2:
            temp = 0
            if layer == 0:
                for column in 0,4,8:
                    if board_dict['data'][column] == to_find: temp += 1
                    if temp == 3:
                        clear('CONGRATS')
            else:
                for column in 2,4,6:
                    if board_dict['data'][column] == to_find: temp += 1
                    if temp == 3:
                        clear('CONGRATS')

        """vertical check"""
        for layer in 1,2,3:
            temp=0
            if layer == 1:
                for column in 0,3,6:
                    if board_dict['data'][column] == to_find: temp += 1
                    if temp == 3:
                        clear('CONGRATS')
            
            elif layer == 2:
                for column in 1,4,7:
                    if board_dict['data'][column] == to_find: temp += 1
                    if temp == 3:
                        clear('CONGRATS')
            else:
                for column in 2,5,8:
                    if board_dict['data'][column] == to_find: temp += 1
                    if temp == 3:
                        clear('CONGRATS')
        
        """full board check"""
        full = 0
        for value in temporary_list:
            if value:
                full += 1
                if full == 9:
                    draw()
            else:
                full = 0
                break

        checking=False
    board_dict['user_turn'] = False if board_dict['user_turn'] else True
    take_turns(board_dict)

def draw():
    clear('nobody won')

if __name__ == '__main__':
    main_menu(GAME_BOARD)