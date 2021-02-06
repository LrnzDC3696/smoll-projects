import os
import random
from time import sleep

RESPONSE = ["As I see it, yes.",
    "Ask again later.",
    "Better not tell you now.",
    "Cannot predict now",
    "Concentrate and ask again",
    "Don't count on it",
    "It is certain",
    "Most likely",
    "My reply is no.",
    "My sources say no",
    "Reply hazy, try again",
    "Signs point to yes",
    "Yes",
    "No",
    "Maybe"
    ]


def clear(last_words='', time=0, stop=True):
    """clears the console"""
    print(last_words)
    if stop:
        input()
    sleep(time)
    os.system('clear')

def main(list_of_responses):
    username = input('Please type your name: ')
    clear(f'Welcome {username}\nPlease type enter tor start the game and REMEMBER TO QUIT PRESS Q')
    ball(list_of_responses)
    
def ball(list_of_responses):
    while True:
    	ans = input('Your Question: ').lower().strip()
    	if ans in ('quit','q'):
    		break
    	print(f'Answer: {list_of_responses[random.randint(0, len(list_of_responses)-1)]}\n')
    print('Thank You for using our 8ball service!')

if __name__ == '__main__':
    main(RESPONSE)
