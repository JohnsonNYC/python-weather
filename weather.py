import requests
from dotenv import load_dotenv
import os

load_dotenv()

def celsius_to_farenheiht(celsius):
  return (celsius - 273.15) * 9 / 5 + 32

def get_weather(city):
  api_key = os.getenv("OPENWEATHERMAP_API_KEY")
  print(api_key)
  url =f"http://api.openweathermap.org/data/2.5/weather?q={city}&APPID={api_key}"
  response = requests.get(url)
  data = response.json()

  if data['cod'] == 200:
    weather = data['weather'][0]['description']
    temperature = data['main']['temp']
    print(f"Weather: {weather}, Temperature: {celsius_to_farenheiht(temperature)}°C")
  else:
    print("City not found")

city = input("Enter a city name: ")
get_weather(city)