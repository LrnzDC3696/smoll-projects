"""My own tic tac toe 2.0"""

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
    'data' : [[],[],[],[],[],[],[],[],[]],
    'game_mode' : 0 #1 if against a bot #0 if against another person
    }

def main_menu(data):
    username = input('Please type your name: ')
    clear(stop=False)
    
    print(f'Welcome {username} please choose the game type:')
    print('1 for against the user cool ai\n2 for 2 player game\n')
    
    """loops until correct"""
    choice = None 
    while choice not in ('1','2'):
        choice = input('Your choice: ')
    clear('Press Enter to Play')
    
    data['game_mode'] = int(choice) - 1
    backend(data, data['game_mode'])
    
    
def backend(data, game_mode):
    call_bot = True if game_mode == 0 else False
    player1_turn = random.choice([True, False])
    winner = None
    draw = None
    """Start Game"""
   
    """repeat while the game is not over"""
    while True:
        
        to_find = 'X' if player1_turn else 'O'
        
        """Checking for win, tie"""
        winner = win_checks(data, to_find, player1_turn)
        draw = draw_check(data)
        if winner: break
        if draw: break
        
        """Taking only the input with checks"""
        print(f'{data["board"]}\n')
        
        some_input = take_input(data['data'],player1_turn, call_bot)
        
        """Updating the board"""
        data['data'][some_input] = 1 if player1_turn else 2
        data['board'] = data['board'].replace(str(some_input + 1), 'X' if player1_turn else 'O')
        
        """Changing Turns"""
        player1_turn = False if player1_turn else True
        
    clear('Thank you for playing')
    
    
def take_input(data_list, player1_turn, call_bot):
    """
    takes 3 arguments
    data_list is the backend list
    player1_turn if true or false
    game_mode is if against the bot or not
    """
    
    while True:
        choice = None
        
        try:
            if player1_turn:
                choice = int(input('Player 1 Choice: '))
            else:
                if call_bot:
                    print('The cool ai Choice:', end=' ')
                    choice = random.randint(1,9)
                    print(choice)
                else:
                    choice = int(input('Player 2 Choice: '))
            if not data_list[int(choice)-1]:
                break
        except:
            pass
        
        print('invalid input')
        
    return choice -1
    
    
def win_checks(game_data, to_find, player_):
    """horizontal check"""
    to_find = 1 if player_ else 2
    for layer in 0,3,6:
        temp = 0
            
        for row in range(layer, layer+3):
                
            if game_data['data'][row] == to_find: temp += 1
            if temp == 3:
                win()
                return True

    """diagonal check"""
    for layer in 0,2:
        temp = 0
        if layer == 0:
            for column in 0,4,8:
                if game_data['data'][column] == to_find: temp += 1
                if temp == 3:
                    win()
                    return True
        else:
            for column in 2,4,6:
                if game_data['data'][column] == to_find: temp += 1
                if temp == 3:
                    win()
                    return True

    """vertical check"""
    for layer in 1,2,3:
        temp=0
        if layer == 1:
            for column in 0,3,6:
                if game_data['data'][column] == to_find: temp += 1
                if temp == 3:
                    win()
                    return True
                    
        elif layer == 2:
            for column in 1,4,7:
                if game_data['data'][column] == to_find: temp += 1
                if temp == 3:
                    win()
                    return True
        else:
            for column in 2,5,8:
                if game_data['data'][column] == to_find: temp += 1
                if temp == 3:
                    win()
                    return True

def draw_check(game_data):
    """full board check"""
    full = 0
    for value in game_data['data']:
        if value:
            full += 1
            if full == 9:
                draw()
                return True
        else:
            return False
    
def draw():
    clear('DRAW')

def win():
    clear('WIN')
    
if __name__ == '__main__':
    main_menu(GAME_BOARD)