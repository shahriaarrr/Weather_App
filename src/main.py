import datetime as dt
import requests
import schedule
#for loading and reading .env file
import dotenv
import os

#load .env file and read API_KEY from .env file
dotenv.load_dotenv()
API_KEY = os.getenv('API_KEY')
#add our URL
BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
#Add a city which weather conditions we want
CITY = "Tehran"

def kelvin_to_celsius(kelvin):
    celsius = kelvin - 273.15


    return celsius

url = BASE_URL + "appid=" + API_KEY + "&q=" + CITY

def check_weather():
    response = requests.get(url).json()

    temp_kelvin = response['main']['temp']
    temp_celsius= kelvin_to_celsius(temp_kelvin)
    feels_like_kelvin = response['main']['feels_like']
    feels_like_celsius = kelvin_to_celsius(feels_like_kelvin)
    wind_speed = response['wind']['speed']
    humidity = response['main']['humidity']
    description = response['weather'][0]['description']
    sunrise_time = dt.datetime.utcfromtimestamp(response['sys']['sunrise'] + response['timezone'])
    sunset_time = dt.datetime.utcfromtimestamp(response['sys']['sunset'] + response['timezone'])

    print(f"Temperature in {CITY}: {temp_celsius:.2f}°C")
    print(f"Temperature in {CITY} feels like: {feels_like_celsius:.2f}°C")
    print(f"Humidity in {CITY} : {humidity}%")
    print(f"Wind Speed in {CITY} : {wind_speed}km/h")
    print(f"General weather in {CITY} : {description}")
    print(f"Sun rises in {CITY} at {sunrise_time} local time")
    print(f"Sun Sets in {CITY} at {sunset_time} local time")
    print(response['sys']['sunset'] + response['timezone'])
    print(response['sys']['sunrise'] + response['timezone'])

schedule.every(5).seconds.do(check_weather)

while True:
    schedule.run_pending()
