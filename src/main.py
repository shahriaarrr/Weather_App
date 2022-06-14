import datetime as dt
import requests

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

url = BASE_URL + "appid=" + API_KEY + "&q=" + CITY

response = requests.get(url).json()

print(response)

