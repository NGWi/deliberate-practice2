import os
import requests
import json
def get_coordinates(address, api_key):
    base_url = "https://maps.googleapis.com/maps/api/geocode/json"
    params = {
        "address": address,
        "key": api_key
    }
    response = requests.get(base_url, params=params)
    data = response.json()
    results = data["results"]
    if len(results) > 0:
        geometry = results[0]["geometry"]
        lat = geometry["location"]["lat"]
        lng = geometry["location"]["lng"]
        return {"latitude": lat, "longitude": lng}
    else:
        return None

api_key = os.environ['GM_KEY']  # Replace with your actual API key
url = f"https://routes.googleapis.com/distanceMatrix/v2:computeRouteMatrix?key={api_key}"

headers = {
    "Content-Type": "application/json",
    "X-Goog-FieldMask": "originIndex,destinationIndex,status,condition,distanceMeters,duration"
}

locations = [
    "San Francisco, CA",
    "Los Angeles, CA",
    "New York, NY",
    "Chicago, IL"
]

geocoded = []
for location in locations:
    geocoded.append({"waypoint": {"location": {"latLng": get_coordinates(location, api_key)}}})


payload = {
    "origins": geocoded,
    "destinations": geocoded,
    "travelMode": "DRIVE"
}

response = requests.post(url, headers=headers, data=json.dumps(payload))

if response.status_code == 200:
    data = response.json()
    for row in data:
        print(row)
    
else:
    print(f"Error: {response.status_code}")
    print(response.text)