import requests
from math import radians, sin, cos, sqrt, atan2



def geocode_location(location_name):
    """
    Hämtar lat/lon för en given ort
    """
    url = "https://nominatim.openstreetmap.org/search"
    params = {
        "q": location_name,
        "format": "json",
        "email": "din.epost@adress.com",
        "limit": 1
    }
    response = requests.get(url, params=params)
    data = response.json()

    if data:
        return {
            "lat": float(data[0]["lat"]),
            "lon": float(data[0]["lon"])
        }
    return None

def haversine_distance(coord1, coord2):
    """
    Beräknar avstånd mellan två koordinater
    """
    R = 6371  # Jordens radie i km

    lat1, lon1 = radians(coord1["lat"]), radians(coord1["lon"])
    lat2, lon2 = radians(coord2["lat"]), radians(coord2["lon"])

    dlat = lat2 - lat1
    dlon = lon2 - lon1

    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    return R * c


def calculate_city_distance(city1, city2):
    """
    Huvudfunktion som orkestrerar båda agenterna
    """
    print(f"Söker koordinater för {city1}...")
    coord1 = geocode_location(city1)

    print(f"Söker koordinater för {city2}...")
    coord2 = geocode_location(city2)

    if coord1 and coord2:
        distance = haversine_distance(coord1, coord2)
        print(f"\nAvstånd: {distance:.2f} km")
        return distance
    else:
        print("Kunde inte hitta en eller båda orterna")
        return None