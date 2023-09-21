import requests

# -------------------- USING API TO LOCATE THE INTERNATIONAL SPACE STATION (ISS) -----------------
response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()

data_iss = response.json()

longitude = data_iss["iss_position"]["longitude"]
latitude = data_iss["iss_position"]["latitude"]

iss_position_tuple = (longitude, latitude)
print(f"The international space station coordinates at the current moment is :{iss_position_tuple}")


# ------------------- USING API TO GET THE SUNRISE AND SUNSET TIME FOR LONDON(WITH COORDINATES) -------------------
LAT = 51.5072
LON = 0.1276

london_coordinates = {
    "lat": LAT,
    "lng": LON,
    "formatted": 0,
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=london_coordinates)
response.raise_for_status()
data_sunrise_sunset = response.json()
sunrise = int(data_sunrise_sunset["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data_sunrise_sunset["results"]["sunset"].split("T")[1].split(":")[0])
print(f"The sunrise for the selected location (London) is at: {sunrise} and sunset is at: {sunset}")
