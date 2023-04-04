import os
import sys

def fibonacci_sequence(n):
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    return fib

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('------------------------------------------------')
    print('           Fibonacci Sequence                   ')
    print('------------------------------------------------')
    print('Enter the number of elements you want in the Fibonnaci sequence: ')
    num = int(input(''))
    fib_sequence = fibonacci_sequence(num)
    print('\n')
    print(fib_sequence)
    print('\n')
    
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


