import os
import sys
import secrets
import string

def generate_token(nbytes):
    alphabet = string.ascii_letters + string.digits
    while True:
        token = secrets.token_urlsafe(nbytes)
        if all(c in alphabet for c in token):
            return token

def user_input():
    while True:
        try:
            nbytes = int(input('Token length (from 8 - 64): '))
        except ValueError:
            print('\nError: Invalid input.\n')
            continue
        
        if nbytes < 8 or nbytes > 64:
            print('\nError: Token length must be between 8 and 64.\n')
            continue
        else:
            token = generate_token(nbytes=nbytes)
            print(f'Generated token: {token} \n')
            break

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('------------------------------------------------')
    print('               Token Generator                  ')
    print('------------------------------------------------')
    user_input()

    while True:
        response = input('Do you want to continue? (Y/N) ')
        if response == 'y' or response == 'Y':
            main()
        elif response == 'n' or response == 'N':
            sys.exit()
        else:
            print('\nError: Please select Y or N.\n')
            continue

if __name__ == '__main__':
    main() 