import os
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
    
def app_header():
    print('------------------------------------------------')
    print('            Guess the number version 2          ')
    print()
    print('  Guess the number from 1 - 100 with 6 attempts ')
    print('------------------------------------------------')
    print()
def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    app_header()
    guess_num = guess_number()
    print()

main()

while True:
    print('Do you want to continue? [y/n]: ',end='')
    check = input()
    if check == 'n' or check == 'N':
        print('\nThanks and have a great day!\n')
        break
    else:
        main()