import os
import sys

def calculate_bmi():
    while True:
        try:
            h = float(input('Your height in meters (ex. 1.73): '))
            break
        except ValueError:
            print('Height must be a number.\n')
    
    while True:
        try:
            w = float(input('Your weight in kilograms (ex. 75): '))
            break
        except ValueError:
            ('Weight must be a number.\n')

    normal_bmi = 'Normal BMI is from 18.50 to 24.90.'
    bmi = w / (h**2)
    bmi = round(bmi, 2)
    
    if bmi < 18.49:
        print('\nYour BODY MASS INDEX is {:0.2f} and classified as SEVERELY UNDERWEIGHT.'.format((bmi)))
        print(normal_bmi)
    elif bmi == 18.49:
        print('\nYour BODY MASS INDEX is {:0.2f} and classified as UNDERWEIGHT.'.format((bmi)))
        print(normal_bmi)
    elif bmi <= 24.99:
        print('\nYour BODY MASS INDEX is {:0.2f} and classified as NORMAL.'.format((bmi)))
    elif bmi <= 29.99:
        print('\n\nYour BODY MASS INDEX is {:0.2f} and classified as OVERWEIGHT.'.format((bmi)))
        print(normal_bmi)
    elif bmi <= 34.99:
        print('\nYour BODY MASS INDEX is {:0.2f} and classified as SEVERELY OVERWEIGHT.'.format((bmi)))
        print(normal_bmi)
    elif bmi <= 39.99:
        print('\nYour BODY MASS INDEX is {:0.2f} and classified as OBESE.'.format((bmi)))
        print(normal_bmi)
    else:
        print('\nYour BODY MASS INDEX is {:0.2f} and classified as SEVERELY OBESE.'.format((bmi)))
        print(normal_bmi)
        return 
def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    app_name = 'BMI Calculator'
    print(f'{"-" * 48}')
    print(f'{" " * 12}{app_name}{" " * 12}')
    print(f'{"-" * 48}')
    calculate_bmi()
    
    while True:
        response = input('\nDo you want to continue? (Y/N) ')
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
