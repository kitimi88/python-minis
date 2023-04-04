import os
import sys
import requests

def convert_currency(amount, from_currency, to_currency):

    url = f'https://api.exchangerate-api.com/v4/latest/{from_currency}'

    response = requests.get(url)
    rates = response.json()['rates']

    converted_amount = amount * rates[to_currency]

    return converted_amount


def user_input():
    amount = float(input("Enter amount: "))
    from_currency = input("Enter the currency to convert FROM (e.g. USD): ").upper()
    to_currency = input("Enter the currency to convert TO (e.g. php): ").upper()

    result = convert_currency(amount, from_currency, to_currency)
    print('\n')
    print(f"{amount:.2f} {from_currency} is equal to {result:.2f} {to_currency}")

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('------------------------------------------------')
    print('           Currency Converter                   ')
    print('------------------------------------------------')
    user_input()
    
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
