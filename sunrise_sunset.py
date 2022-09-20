import requests
from datetime import datetime, time
import smtplib
import time
#TODO-1 Sunrise-sunset my own time setup
my_lat = 34.410734
my_lon = 35.848680
#its not required after there update
parameters = {
    "lat": my_lat ,
    "long": my_lon,
    "formatted":0
}
my_time = datetime.now()
hour_clock = my_time.hour
print(hour_clock )
response = requests.get(url="https://api.sunrise-sunset.org/json",params=parameters)
response.raise_for_status()
data = response.json()
sunrise_time = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset_time = int(data["results"]["sunset"].split("T")[1].split(":")[0])
print(sunrise_time)
print(sunset_time)
#TODO-2 Setup for the iss position
response2 = requests.get(url="http://api.open-notify.org/iss-now.json")
response2.raise_for_status()
data2 = response2.json()
long_iss = data2["iss_position"]["longitude"]
lat_iss = data2["iss_position"]["latitude"]
position_iss = (long_iss, lat_iss)
print(position_iss)
#TODO-3 putting myposition in a tuple and my email data
my_email = #Add your email
password = #add the pass generated from google
receiver_mail = #add the receiver email 
my_position = (my_lon,my_lat)
print(my_position)
#TODO-CONDITION TO CATCH THE ISS WITH MY OWN TIME AND PLACE
while True:
    time.sleep(60)
    if my_position == position_iss:
        if hour_clock > sunset_time and hour_clock < sunrise_time:
            with smtplib.SMTP("smtp.gmail.com", 587) as connection:
                connection.starttls()
                connection.login(user=my_email, password=password)
                connection.sendmail(from_addr=my_email,
                                    to_addrs=receiver_mail,
                                    msg=f"Subject:ISS_IS_ABOVE\n\n Look above it'is here")

#TODO - WE CAN IMPROVE THIS CODE BY ADDING FUNCTION FOR EVER TODO AND RETURN TRUE FOR EVERY FUNCTION

