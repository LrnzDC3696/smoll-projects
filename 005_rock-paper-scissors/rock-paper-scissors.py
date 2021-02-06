import os
import random
from time import sleep

rpc = {
    0:"Rock",
    1:"Paper",
    2:"Scissors"
}

def clear(last_words='', time=0, stop=True):
    """clears the console"""
    print(last_words)
    if stop:
        input()
    sleep(time)
    os.system('clear')

def main(choices):
    username = input('Please type your name: ')
    clear(f'Welcome {username} Please type enter tor start the game')
    game(choices)
    
def game(choices):
    while True:
        print("Choices:\n(0) Rock\n(1) Paper\n(2) Scissors\n(3) Quit\n")
    
        bot_choice = random.randint(0,2)
        try:
            user_choice = int(input("Choice:"))
        except ValueError:
            print("Invalit Input Try Again\n")
            continue
        
        if user_choice == 3:
            print("Thank you for quiting")
            break
        
        print(f"Bot chose {choices[bot_choice]}\nYou chose {choices[user_choice]}\n")
        
        #checks
        if bot_choice == user_choice:
            print(f"You both chose {choices[user_choice]}\n !!!TIE!!!\n")
        
        elif ((user_choice + 1) % 3) == bot_choice:
            print(f"{choices[bot_choice]} beats {choices[user_choice]}\n !!!YOU LOSE!!!\n")
        
        else:
            print(f"{choices[user_choice]} beats {choices[bot_choice]}\n !!!YOU WIN!!! \n")

        clear('press enter to continue')

if __name__ == '__main__':
    main(rpc)
    