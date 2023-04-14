import os
import sys

error_msg = '\n[!] ERROR: Invalid option. Please try again.\n'
error_msg2 = '\n[!] ERROR: Must be a positive integer.\n'

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

def get_positive_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            if not value.is_integer:
                print(error_msg2)
                continue
            return value
        except ValueError:
            print(error_msg)

def user_input():
    while True:
        print("Please select an operation:")
        print("[1] Add")
        print("[2] Subtract")
        print("[3] Multiply")
        print("[4] Divide")
        print("[5] Quit")
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            a = get_positive_input("First Num: ")
            b = get_positive_input("Second Num: ")
            print("\nSum: {:0.2f}".format(add(a,b)))
            break
        
        elif choice == "2":
            a = get_positive_input("First Num: ")
            b = get_positive_input("Second Num: ")
            print("\nDifference: {:0.2f}".format(subtract(a,b)))
            break

        elif choice == "3":
            a = get_positive_input("First Num: ")
            b = get_positive_input("Second Num: ")
            print("\nProduct: {:0.2f}".format(multiply(a,b)))
            break

        elif choice == "4":
            a = get_positive_input("First Num: ")
            b = get_positive_input("Second Num: ")
            try:
                print("\nQuotient: {:0.2f}".format(divide(a,b)))
            except ValueError as e:
                print(e)
                break
        
        elif choice == "5" or choice == 'exit':
            print("Thank you and have a great day!")
            sys.exit()
        else:
            print(error_msg)
            break
        

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    app_name = 'Simple Calculator'
    print(f'{"-" * 48}')
    print(f'{" "*10}{app_name}{" "*10}')
    print(f'{"-" * 48}')
    user_input()

    while True:
        response = input('\nDo you want to continue? (Y/N)')
        if response == 'y' or response == 'Y':
            main()
        elif response == 'n' or response == 'N' or response == 'exit':
            print('\nThank you and have a great day.\n')
            sys.exit()
        else:
            print('\nError: Please select Y or N.\n')
            continue

if __name__ == '__main__':
    main() 