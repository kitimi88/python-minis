import os
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
            break

def app_header():
    print('------------------------------------------------')
    print('            Guess the number                    ')
    print()
    print('------------------------------------------------')
    print('     MECHANICS: Guess a number from 1 - 100     ')
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
    if check == 'y' or check == 'Y':
        main()
        
    elif check == 'n' or check == 'N':
        print('\nThanks and have a great day!\n')
        break
    else:
        print('\nPlease select y or n.')
        continue

