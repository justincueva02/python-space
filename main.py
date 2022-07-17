import requests
from datetime import datetime

parameters = {
    "formatted": 0,
}

response = requests.get(url="https://api.sunrise-sunset.org/json?lat=34.089386&lng=-117.872338", params=parameters)
response.raise_for_status()
data = response.json()["results"]
sunrise = data["sunrise"]
sunset = data["sunset"]

print(sunrise.split("T")[1].split(":")[0])
print(sunset.split("T")[1].split(":")[0])

time_now = datetime.now()
print(time_now.hour)
