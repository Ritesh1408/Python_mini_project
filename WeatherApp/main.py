import requests
import json
import pyttsx3

city = input("Enter the city name: \n ")
url = f"https://api.weatherapi.com/v1/current.json?key=2124e5cbc1454338aaa112454240403&q={city}"
response = requests.get(url)
wdic = json.loads(response.text)

temperature = wdic['current']['temp_c']
condition = wdic['current']['condition']['text']
feelslike = wdic['current']['feelslike_c']
pyttsx3.speak(f"The temperature in {city} is {temperature} degrees Celsius. The weather condition is {condition}. and its feels like {feelslike} degrees Celsius")
