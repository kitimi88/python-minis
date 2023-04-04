import os
import sys

def calculate_bmi():
    while True:
        try:
            h = float(input('Your height in meters: '))
            break
        except ValueError:
            print('Height must be a number.\n')
    
    while True:
        try:
            w = float(input('Your weight in kilograms: '))
            break
        except ValueError():
            ('Weight must be a number.\n')

    bmi = w / (h**2)
    bmi = round(bmi, 2)
    
    if bmi < 18.4:
        print('\nYour BODY MASS INDEX is {:0.2f} and classified as SEVERELY UNDERWEIGHT.'.format((bmi)))
    elif bmi == 18.4:
        print('\nYour BODY MASS INDEX is {:0.2f} and classified as UNDERWEIGHT.'.format((bmi)))
    elif bmi <= 24.9:
        print('\nYour BODY MASS INDEX is {:0.2f} and classified as NORMAL.'.format((bmi)))
    elif bmi <= 29.9:
        print('\n\nYour BODY MASS INDEX is {:0.2f} and classified as OVERWEIGHT.'.format((bmi)))
    elif bmi <= 34.9:
        print('\nYour BODY MASS INDEX is {:0.2f} and classified as SEVERELY OVERWEIGHT.'.format((bmi)))
    elif bmi <= 39.9:
        print('\nYour BODY MASS INDEX is {:0.2f} and classified as OBESE.'.format((bmi)))
    else:
        print('\nYour BODY MASS INDEX is {:0.2f} and classified as SEVERELY OBESE.'.format((bmi)))
        return 
def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('------------------------------------------------')
    print('           BMI Calculator                       ')
    print('------------------------------------------------')
    calculate_bmi()
    
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
