import os

def fibonacci_sequence(n):
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    return fib

def app_header():
    print('------------------------------------------------')
    print('          Fibonacci Sequence                    ')
    print('------------------------------------------------')
    print()

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    app_header()
    print('Enter the number of elements you want in the Fibonnaci sequence:')
    num = int(input(''))
    fib_sequence = fibonacci_sequence(num)
    print('\n')
    print(fib_sequence)
    print('\n')

main()

while True:

    print('Do you want to continue? [y/n]: ',end='')
    check = input()
    if check == 'y' or check == 'Y':
        main()
        
    elif check == 'n' or check == 'N':
        print('\nThanks for playing. Have a great day!\n')
        break
    else:
        print('\nPlease select y or n.')
        continue

