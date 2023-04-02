import os
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
            print("Congratulations! You guessed the word.")
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

# Start the game
# play_game()

def app_header():
    print('------------------------------------------------')
    print('                 Hangman                        ')
    print('------------------------------------------------')
    print()

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    app_header()
    play_now = play_game()
    print()

main()

while True:
    print('Continue playing? [y/n]: ',end='')
    check = input()
    if check == 'y' or check == 'Y':
        main()
    
    elif check == 'n' or check == 'N':
        print('\nThank you and have a great day!\n')
        break
    else:
        print('\nPlase select y or n.')
        continue