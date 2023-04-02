import os
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

def app_header():
    print('------------------------------------------------')
    print('           Password Generator                   ')
    print('------------------------------------------------')
    print()

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    app_header()
    user_input()
    print()
    
main()

while True:
    print('Generate another password? [y/n]: ',end='')
    check = input()
    if check == 'y' or check == 'Y':
        main()
    
    elif check == 'n' or check == 'N':
        print('\nThank you and have a great day!\n')
        break
    else:
        print('\nPlase select y or n.')
        continue