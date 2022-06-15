import datetime as dt
import requests
import schedule
# for loading and reading .env file
from dotenv import load_dotenv
import os
# for working with MYSQL database
import mysql.connector

# connect to MYSQL database
print("connecting to db...")
cnx = mysql.connector.connect(user='{username}', password='{password}',
                              # if your database in your local system you can skip the ((host)) field
                              host='127.0.0.1',
                              database='{database name}')
print("connected to db")
cursor = cnx.cursor()

# load .env file and read API_KEY from .env file
load_dotenv()
API_KEY = os.getenv('API_KEY')

# add our base URL
BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"

# Add a city which weather conditions we want
CITY = "Tehran"

# Convert Kelvin to Celsius
def kelvin_to_celsius(kelvin):
    celsius = kelvin - 273.15
    return celsius

# Create a URL to send a request
url = BASE_URL + "appid=" + API_KEY + "&q=" + CITY

# our main function
def main():
    print("getting information from openweather...")
    # send request and save json response
    response = requests.get(url).json()

    # get our needed info from response
    temp_kelvin = response['main']['temp']
    temp_celsius = float(f"{kelvin_to_celsius(temp_kelvin):.2f}")
    feels_like_kelvin = response['main']['feels_like']
    feels_like_celsius = kelvin_to_celsius(feels_like_kelvin)
    wind_speed = response['wind']['speed']
    humidity = response['main']['humidity']
    description = response['weather'][0]['description']
    sunrise_time = dt.datetime.utcfromtimestamp(response['sys']['sunrise'] + response['timezone'])
    sunset_time = dt.datetime.utcfromtimestamp(response['sys']['sunset'] + response['timezone'])
    
    print("get all information from openweather API")

    # execute and commit datas to database
    command = f"INSERT INTO ((table name)) VALUES ({temp_celsius}, {humidity}, {wind_speed}, '{description}', '{sunrise_time}', '{sunset_time}')"
    cursor.execute(command)
    cnx.commit()

# run main function every 24hours
schedule.every(24).hours.do(main)

# run schedule function
while True:
    schedule.run_pending()
