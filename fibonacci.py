import os
import sys

def fibonacci_sequence(n):
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    return fib

def user_input():
    while True:
        try:
            num = int(input('Enter number from 6 to 50: '))
            break
        except ValueError:
            print('\nError: Input must be a number.\n')
            return
    
    if num <= 5 or num >= 51:
        print('\nError: Input between 6 to 50.\n')
        return
             
    fib_sequence = fibonacci_sequence(num)
    print()
    print(fib_sequence)
    print()

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('------------------------------------------------')
    print('           Fibonacci Sequence                   ')
    print('------------------------------------------------')
    user_input()
    
    while True:
        response = input('Do you want to continue (Y/N)? ')
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