import requests
import os
from dotenv import load_dotenv
load_dotenv('./.env')


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

    city = input('Enter city name: ')
    weather = get_weather(city)


    if weather:
        print(f"\nCurrent weather in {weather['city']}:")
        print(f"Description: {weather['description']}")
        print(f"Temperature: {weather['temperature']} °C")
        print(f"Humidity: {weather['humidity']}%")
        print(f"Wind speed: {weather['wind_speed']} m/s")
    else:
        print(f"Could not retrieve weather information for {city}")
        


def app_header():
    print('------------------------------------------------')
    print('                     Weather                    ')
    print('------------------------------------------------')
    print()

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    app_header()
    g_city = get_city()
    g_weather = get_weather(g_city)
    print()

main()

while True:

    print('Check another city? [y/n]: ',end='')
    check = input()
    if check == 'y' or check == 'Y':
        main()
        
    elif check == 'n' or check == 'N':
        print('\nThanks and have a great day!\n')
        break
    else:
        print('\nPlease select y or n.')
        continue