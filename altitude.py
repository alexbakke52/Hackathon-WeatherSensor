import requests

def get_altitude(latitude, longitude):
    url = f"https://api.open-elevation.com/api/v1/lookup?locations={latitude},{longitude}"
    response = requests.get(url)
    data = response.json()
    if 'results' in data and len(data['results']) > 0:
        altitude = data['results'][0]['elevation']
        return altitude
    else:
        return None

latitude = 50.771839672338054  # Replace with your latitude
longitude = 6.08975644004863  # Replace with your longitude

altitude = get_altitude(latitude, longitude)
if altitude is not None:
    print("Altitude:", altitude, "meters")
else:
    print("Failed to retrieve altitude.")