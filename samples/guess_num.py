import os
import sys
import random

def guess_number():
    secret_number = random.randint(1, 100)
    num_guesses = 0


    while True:
        try:
            guess = int(input('Pick a number: '))
            
        except ValueError:
            print('Invalid. Input must be a number.')
            continue

        num_guesses +=1

        if guess < secret_number:
            print('\nToo LOW! Try again.\n')
        elif guess > secret_number:
            print('\nToo HIGH! Try again.\n')
        else:
            print(f'\nAwesome! The correct answer is {secret_number} and you got it in {num_guesses} attempts.')
            print('\n')
            break

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    app_name = 'Guess the number'
    print(f'{"-" * 48}')
    print(f'{" " * 12}{app_name}{" " * 12}')
    print(f'{"-" * 48}')
    guess_number()
    
    while True:
        response = input('Do you want to continue? (Y/N)')
        if response == 'y' or response == 'Y':
            main()
        elif response == 'n' or response == 'N':
            print('\nThank you and have a great day.\n')
            sys.exit()
        else:
            print('\nError: Please select y or n.\n')
            continue

if __name__ == '__main__':
    main()
