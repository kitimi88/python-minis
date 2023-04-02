import os
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

def app_header():
    print('------------------------------------------------')
    print('           Currency Converter                   ')
    print('------------------------------------------------')
    print()

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    app_header()
    user_input()
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