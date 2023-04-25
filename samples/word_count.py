import os
import sys

def count(text):
    words = text.split()
    num_words = len(words)
    num_chars = len(text)
    return num_words, num_chars

def get_user_input():

    user_input = input("Enter text: ")
    num_words, num_chars = count(user_input)
    print("\nTotal word(s):", num_words)
    print("Total character(s):", num_chars)

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    app_name = 'Count Words & Characters'
    print(f'{"-" * 48}')
    print(f'{" " * 12}{app_name}{" " * 12}')
    print(f'{"-" * 48}')
    get_user_input()
    
    while True:
        response = input('\nDo you want to continue? (Y/N) ')
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
