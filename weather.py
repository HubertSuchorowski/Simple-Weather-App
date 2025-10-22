import requests

class Weather:

    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude

    def get_weather(self):
        WeatherUrl = "https://api.open-meteo.com/v1/forecast"

        WeatherParms = {
            "latitude": self.latitude,
            "longitude": self.longitude,
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
