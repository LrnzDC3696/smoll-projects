
import os
import random
from time import sleep
from words import WORDS

HANG_GUY = [
'''
       +---+
           |
           |
           |
         ===
''','''
       +---+
       O   |
           |
           |
         ===
''','''
       +---+
       O   |
       |   |
           |
         ===
''','''
       +---+
       O   |
      /|   |
           |
         ===
''','''
       +---+
       O   |
      /|\  |
           |
         ===
''','''
       +---+
       O   |
      /|\  |
      /    |
         ===
''','''
       +---+
       O   |
      /|\  |
      / \  |
         ===
'''
    ]
def clear(last_words='', time=0, stop=True):
    """clears the console"""
    print(last_words)
    if stop:
        input()
    sleep(time)
    os.system('clear')

def main(wordlist, hangguy):
    username = input('Please put in your name: ')
    clear(stop=False)
    choice = input(f'Welcome {username}\nPlease "enter" to start the game or "q" to quit').lower()
    clear(stop=False)
    
    if choice == 'q':
        return
    
    while True:
        backend(wordlist, hangguy)
        choice = input('do you want to play again? [Y for yes Everything else for No]').lower()
        if choice == 'y':
            continue
        break

def backend(wordlist, hangguy):
    to_guess = randomised_word(wordlist)
    
    hidden = list(to_guess)
    to_show = ['_' for x in hidden]
    tested = set()
    trials = 0
    
    while True:
        print('Becareful of what you type for!')
        print(hangguy[trials])
        print(f'Tested -> "{tested}", Trials -> "{trials}"')
        print('Word -> ', end=' ')
        for character in to_show: print(character, end=',')
        
        choice = input('\nYour choice: ').lower()
     
        if choice == to_guess:
            win(to_guess)
            break
        
        count = 0
        while True:
            temp_word = to_guess
            temp_location = temp_word.find(choice)
            
            if temp_location < 0:
                if not count:
                    trials += 1
                tested.add(choice)
                break
            
            if choice:
                temp_word.replace(choice, '')
                to_show[temp_location] = choice
            count += 1
            break

        if trials > 5:
            lose(to_guess)
            break
        
        clear(stop=False)
        
def randomised_word(wordlist):
    return random.choice(wordlist)

def win(word):
    clear(f'\nThe word was {word}\nyou have won press enter to continue')

def lose(word):
    clear(f'\nThe word was {word}\nyou have lost press enter to continue')

if __name__ == '__main__':
    main(WORDS, HANG_GUY)