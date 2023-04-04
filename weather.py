import requests
import os
import sys
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
        
def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('------------------------------------------------')
    print('                  Weather                       ')
    print('------------------------------------------------')
    g_city = get_city()
    g_weather = get_weather(g_city)
    
    while True:
        response = input('Check another city? (Y/N): ')
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