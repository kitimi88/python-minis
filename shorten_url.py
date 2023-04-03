import os
import re
import pyshorteners

def short_url():
    url_pattern = re.compile(r'^https?://[^\s/$.?#].[^\s]*$')
    s = pyshorteners.Shortener()

    while True:
        url = input('Enter a URL to shorten: ')

        if url_pattern.match(url):
            short_url = s.tinyurl.short(url)
            print('\nShortened URL: ', short_url)
            break
        else:
            print('\nInvalid URL. Please try again.\n')
            

def app_header():
    print('------------------------------------------------')
    print('              URL Shortener                    ')
    print('------------------------------------------------')
    print()

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    app_header()
    s_url = short_url()
    print()

main()

while True:

    print('Do you want to continue? [y/n]: ',end='')
    check = input()
    if check == 'y' or check == 'Y':
        main()
        
    elif check == 'n' or check == 'N':
        print('\nThanks and have a great day!\n')
        break
    else:
        print('\nPlease select y or n.')
        continue


