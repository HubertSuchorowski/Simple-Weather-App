import requests

def Welcome():
    print("Welcome in this Simple Weather App")
    print("Write your City to see current weather")

Welcome()

while True:

    CityName = str(input("Enter City Name: "))

    CITYurl = "https://geocoding-api.open-meteo.com/v1/search"
    GeoParms = {
        "name": CityName,
        "count": 1,
        "language": "pl",
        "format": "json"
    }

    try:
        geoLocation = requests.get(CITYurl, GeoParms) #tworzymy obiekt przechowujący nasze parametry i api
        dataGeo = geoLocation.json() #tworzymy kolejny obiekt w celu uzywania go do logiki


        if dataGeo.get("results"):
            data = dataGeo.get("results")[0]
            latitude = data["latitude"]
            longitude = data["longitude"]
            print(f"Latitude: {data['latitude']}, Longitude: {data['longitude']}")
            break
        else:
            print("You entered the city name incorrectly. Please enter it again and watch out for typos.")



    except requests.exceptions.RequestException as e:
        print(f"Błąd połączenia z Geocoding API: {e}")
        exit()

WeatherUrl = "https://api.open-meteo.com/v1/forecast"

WeatherParms = {
    "latitude": latitude,
    "longitude": longitude,
    "current": "temperature_2m,wind_speed_10m",
    "forecast_days": 1
}

try:
    WeatherStatus = requests.get(WeatherUrl, WeatherParms)
    dataWeather = WeatherStatus.json()

    WeatherData = {
        "temperature": dataWeather["current"]["temperature_2m"],
        "windSpeed": dataWeather["current"]["wind_speed_10m"]
    }

    print("\n--- Aktualna pogoda ---")
    print(f"Temperatura: {WeatherData['temperature']}")
    print(f"WindSpeed: {WeatherData['windSpeed']}")

except requests.exceptions.RequestException as e:
    print(f"Błąd połączenia z Weather API: {e}")
    exit()
