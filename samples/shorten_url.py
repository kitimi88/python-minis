import os
import re
import sys
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
            
def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    app_name = 'URL Shortener'
    print(f'{"-" * 48}')
    print(f'{" " * 12}{app_name}{" " * 12}')
    print(f'{"-" * 48}')
    short_url()
    
    while True:
        response = input('\nDo you want to continue? (Y/N)')
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
