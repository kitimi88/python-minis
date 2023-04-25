import os
import sys
import requests
from dotenv import load_dotenv
load_dotenv('./.env')
import datetime

api_key = os.environ['OPENWEATHER_API_KEY'] 

def get_weather(city):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        weather = {
            'city': data['name'],
            'description': data['weather'][0]['description'],
            'temperature': data['main']['temp'],
            'humidity': data['main']['humidity'],
            'wind_speed': data['wind']['speed'],
        }
        return weather
    else:
        return None

def get_city():
    today = datetime.date.today()

    city = input('Enter city name: ')
    weather = get_weather(city)


    if weather:
        print(f"\nAs of: ",today)
        print(f"Current weather in {weather['city']}:")
        print(f"Description: {weather['description']}")
        print(f"Temperature: {weather['temperature']} °C")
        print(f"Humidity: {weather['humidity']}%")
        print(f"Wind speed: {weather['wind_speed']} m/s")
    else:
        print(f"Could not retrieve weather information for {city}")
        
def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    app_name = 'Weather'
    print(f'{"-" * 48}')
    print(f'{" " * 12}{app_name}{" " * 12}')
    print(f'{"-" * 48}')
    get_city()
    
    while True:
        response = input('\nCheck another city? (Y/N): ')
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