import os
import sys
import random

def guess_number():
    secret_number = random.randint(1, 100)

    for i in range(6):
        guess = int(input('Pick a number: '))

        if guess < secret_number:
            print('\nToo LOW! Try again.\n')
        elif guess > secret_number:
            print('\nToo HIGH! Try again.\n')
        else:
            print("\nCongratulations! You got it!")
            return

    print(f"Sorry, you ran out of guesses. The number was {secret_number}.\n")

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('------------------------------------------------')
    print('             Guess the number v2                ')
    print('------------------------------------------------')
    guess_num = guess_number()
    
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

