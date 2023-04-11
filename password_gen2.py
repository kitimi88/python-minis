import os
import sys
import random
import string

def generate_password(complexity,length):
    while True:
        
        if complexity == '1': # weak
            characters = string.ascii_letters
        elif complexity == '2': # medium
            characters = string.ascii_letters + string.digits
        elif complexity == '3': # strong
            characters = string.ascii_letters + string.digits + string.punctuation
        else:
            
            print('\nError: Please choose [1] weak, [2] medium [3] strong.\n')
            break

        password = ''.join(random.choice(characters) for _ in range(length))
        return password

def user_input():
    while True:
        try:
            length = int(input("\nEnter password length (min. 8 max. 64): "))
            break
        except ValueError:
            print('\nError: Password length must be a number.\n')
            return
    
    if length <= 7 or length >= 65:
        print('\nError: Required length did match.\n')
        return

    
    print('\nComplexity level:\n [1] Weak\n [2] Medium\n [3] Strong\n')
    complexity = input('')
    password = generate_password(length=length, complexity=complexity)
    if password is None:
        print('')
    else:
        print('\nYour password is:',(password))
        print()

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('------------------------------------------------')
    print('           Password generator v2                ')
    print('------------------------------------------------')
    user_input()

    while True:
        response = input('Do you want to continue? (Y/N) ')
        if response == 'y' or response == 'Y':
            main()
        elif response == 'n' or response == 'N':
            print('\nThank you and have a great day!\n')
            sys.exit()
        else:
            print('\nError: Please select Y or N.\n')
            continue

if __name__ == '__main__':
    main()