import os

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

def app_header():
    print('------------------------------------------------')
    print('           Count Words & Characters             ')
    print('------------------------------------------------')
    print()

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    app_header()
    get_user_input()
    print()
    
main()

while True:
    print('Do you want to continue? [y/n]: ',end='')
    check = input()
    if check == 'y' or check == 'Y':
        main()
    
    elif check == 'n' or check == 'N':
        print('\nThank you and have a great day!\n')
        break
    else:
        print('\nPlase select y or n.')
        continue