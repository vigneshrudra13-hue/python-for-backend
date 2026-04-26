import requests
import os
from env_loader import get


def currentweather():
    print("*************** Current weather ***************\n")
    city = input("Please enter the city name: ")

    api_key = get('API')
    if not api_key:
        print('API key not found. Make sure .env exists and contains API=...')
        return

    # Use the Current Weather Data endpoint and metric units
    request_url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    

    resp = requests.get(request_url)
    if resp.status_code != 200:
        print(f'Error fetching weather: {resp.status_code} - {resp.text}')
        return

    data = resp.json()
    # Print a concise, human-friendly summary
    name = data.get('name')
    weather = data.get('weather', [{}])[0].get('description')
    main = data.get('main', {})
    temp = main.get('temp')
    feels = main.get('feels_like')
    humidity = main.get('humidity')
    wind = data.get('wind', {}).get('speed')

    print(f"Weather for {name}: {weather}")
    print(f"Temperature: {temp} °C (feels like {feels} °C)")
    print(f"Humidity: {humidity}%")
    print(f"Wind speed: {wind} m/s")


if __name__ == '__main__':
    currentweather()