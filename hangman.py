import os
import sys
import random

with open('hangman_word_list.txt','r') as f:
    word_list = [word.strip() for word in f.readlines()]

word = random.choice(word_list)


def choose_word(word_list):
    return random.choice(word_list)


def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

# Function to get a letter from the user
def get_letter():
    letter = input("\nGuess a letter: ").lower()
    if not letter.isalpha() or len(letter) != 1:
        print("Invalid input! Please enter a single letter.")
        return get_letter()
    else:
        return letter

# Function to play the game
def play_game():
    word = choose_word(word_list)
    guessed_letters = set()
    attempts = 6
    while attempts > 0:
        print("Attempts left:", attempts)
        display = display_word(word, guessed_letters)
        print(display)
        if "_" not in display:
            print("You got it! Awesome.")
            return
        letter = get_letter()
        if letter in guessed_letters:
            print("You already guessed that letter!")
        elif letter in word:
            guessed_letters.add(letter)
            print("Good guess!")
        else:
            attempts -= 1
            guessed_letters.add(letter)
            print("Sorry, that letter is not in the word.")
    print("You ran out of attempts. The word was", word)

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('------------------------------------------------')
    print('               The Hangman                      ')
    print('------------------------------------------------')
    play_now = play_game()
    
    while True:
        response = input('Do you want to continue? (Y/N)')
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
