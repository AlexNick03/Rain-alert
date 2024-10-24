import requests
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()
send_addr = os.getenv('SEND_ADDR')
my_address = os.getenv("MY_ADDR")
my_password = os.getenv("MY_PSS")
MY_LNG = os.getenv("LNG")
MY_LAT = os.getenv("LAT")
api_key = os.getenv("API_KEY")
rain_chances = False
parameters ={
    "lat": MY_LAT,
    "lon": MY_LNG,
    "appid": api_key,
    "units": "metric",
    "cnt": 5
}
response = requests.get("https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
weather_data = response.json()
for forecast in weather_data["list"]:
    if forecast["weather"][0]["id"] < 700:
        rain_chances = True

if rain_chances:
    with smtplib.SMTP('smtp.gmail.com', 587) as connection:
        connection.starttls()
        connection.login(user=my_address, password=my_password)
        connection.sendmail(
            from_addr=my_address,
            to_addrs=send_addr,
            msg="Subject: Hey, it's gonna rain today")
