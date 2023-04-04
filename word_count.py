import os
import sys

def count(text):
    words = text.split()
    num_words = len(words)
    num_chars = len(text)
    return num_words, num_chars

def get_user_input():

    user_input = input("Enter some text: ")
    num_words, num_chars = count(user_input)
    print("\nTotal word(s):", num_words)
    print("Total character(s):", num_chars)

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('------------------------------------------------')
    print('           Count Words & Characters             ')
    print('------------------------------------------------')
    get_user_input()
    
    while True:
        response = input('Do you want to continue? (Y/N) ')
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
