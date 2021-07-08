# Guess the number game
import random

def run():
    random_number = random.randint(1,100)
    player_number = int(input('Select a number between 1 and 100: '))

    while player_number != random_number:
        if player_number < random_number:
            print('Select a bigger number')
        else: 
            print('Select a lower number')
        player_number = int(input('Select another number: '))
    print('You win!')


if __name__ == '__main__':
    run()

