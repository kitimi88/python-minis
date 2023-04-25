import os
import sys

def caesar_cipher(message,shift):

    encrypted_message = ''
    for char in message:
        if char.isalpha():

            shifted_char = chr((ord(char) - 65 + shift) % 26 + 65)
            encrypted_message += shifted_char
        else:
            encrypted_message += char
    return encrypted_message

def user_input():
    plain_message = input('Message you want to encrypt: ')

    while True:
        try:
            shift = int(input('Enter shift value (1-25): '))
        except ValueError:
            print('Error: Shift value must be a number.\n')
            continue
        
        if shift < 1 or shift > 25:
            print('Error: minimum shift value must be between 1 and 25.\n')
            continue
        else:
            encrypted_message = caesar_cipher(plain_message.upper(),shift)
            print('\nYour encrypted message: ', encrypted_message)
            break

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    app_name = 'Message Encryption Tool'
    print(f'{"-" * 48}')
    print(f'{" " * 12}{app_name}{" " * 12}')
    print(f'{"-" * 48}')
    user_input()

    while True:
        print('\nEncrypt another message? (Y/N): ',end='')
        check = input()
        if check == 'y' or check == 'Y':
            main()
        elif check == 'n' or check == 'N':
            print('\nThanks for playing. Have a great day!\n')
            sys.exit()
        else:
            print('\nPlease select y or n.')
            continue

if __name__ == '__main__':
    main()