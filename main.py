import requests
from city import City
from weather import Weather

def Welcome():
    print("Welcome in this Simple Weather App")
    print("Write your City to see current weather")

Welcome()

while True:
    city_name = input("\n📍 Enter the name of the city: ")

    city = City(city_name)

    if city.get_coordinates():
        break
    else:
        print("You entered the city name incorrectly. Please enter it again and watch out for typos.")

weather = Weather(longitude=city.longitude, latitude=city.latitude)
weather.get_weather()
