import requests

class City:
    def __init__(self, name,):
        self.name = name

    def get_coordinates(self):
        CITYurl = "https://geocoding-api.open-meteo.com/v1/search"
        GeoParms = {
            "name": self.name,
            "count": 1,
            "language": "pl",
            "format": "json"
        }
        try:
            geoLocation = requests.get(CITYurl, GeoParms)  # tworzymy obiekt przechowujący nasze parametry i api
            dataGeo = geoLocation.json()  # tworzymy kolejny obiekt w celu uzywania go do logiki

            if dataGeo.get("results"):
                data = dataGeo.get("results")[0]
                self.latitude = data["latitude"]
                self.longitude = data["longitude"]
                print(f"Latitude: {data['latitude']}, Longitude: {data['longitude']}")
                return True
            else:
                return False
        except requests.exceptions.RequestException as e:
            print(f"Błąd połączenia z Geocoding API: {e}")
            exit()