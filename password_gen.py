import os
import sys
import random
import string

def generate_password(length, include_digits=True, include_symbols=True):


    characters = string.ascii_letters  # all letters

    if include_digits:
        characters += string.digits  # add digits
    if include_symbols:
        characters += string.punctuation  # add symbols

    # Generate the password
    password = ''.join(random.choice(characters) for _ in range(length))

    return password

def user_input():
    #password length
    while True:
        try:
            length = int(input("Enter the desired length of your password: "))
            break
        except ValueError:
            print('Input must be a number.\n')

    #include digits
    while True:
        include_digits = input("Include digits? [y/n]: ")
        if include_digits == 'y' or include_digits == 'n':
            break
        else:
            print('Invalid input. Please enter y or n.')
    
    #include symbols
    while True:
        include_symbols = input("Include symbols? [y/n]: ")
        if include_symbols == 'y' or include_symbols == 'n':
            break
        else:
            print('Invalid input. Please enter y or n.')

    password = generate_password(length, include_digits=include_digits, include_symbols=include_symbols)
    print("\nYour password is:", password)
    print('\n')

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('------------------------------------------------')
    print('           Password Generator                   ')
    print('------------------------------------------------')
    user_input()
    
    while True:
        response = input('Generate another password? (Y/N)')
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
