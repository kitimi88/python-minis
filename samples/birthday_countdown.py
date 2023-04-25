import os
import sys
import datetime

def get_user_birthday():
    birthday_str = input("Please enter your birthday (YYYY-MM-DD): ")
    birthday = datetime.datetime.strptime(birthday_str, "%Y-%m-%d").date()

    today = datetime.date.today()
    next_birthday = datetime.date(today.year, birthday.month, birthday.day)
    if next_birthday < today:
        next_birthday = datetime.date(today.year + 1, birthday.month, birthday.day)
    days_until_birthday = (next_birthday - today).days
    age = today.year - birthday.year - ((today.month, today.day) < (birthday.month, birthday.day))


    if days_until_birthday == 0:
        print("Happy {} st/nd/th birthday!".format(age))
    elif days_until_birthday == 1:
        print("Your {} st/nd/th birthday is tomorrow!".format(age))
    else:
        print("Your {} st/nd/th birthday is in {} days.".format(age, days_until_birthday))

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    app_name = 'Birthday Countdown'
    print(f'{"-" * 48}')
    print(f'{" " * 12}{app_name}{" " * 12}')
    print(f'{"-" * 48}')
    get_user_birthday()
    
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
