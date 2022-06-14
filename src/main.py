import datetime as dt
import requests

#for loading and reading .env file
import dotenv
import os

#load .env file and read API_KEY from .env file
dotenv.load_dotenv()
API_KEY = os.getenv('API_KEY')

#add our URL
BASE_URL = "http://api.openweathermap.org/data/3.0/weather?"

#Add a city which weather conditions we want
CITY = "Mashhad"



