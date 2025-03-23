import requests
from datetime import datetime, timedelta
import time
import smtplib





MY_LAT = 31.996754 # Your latitude
MY_LONG = 71.178692 # Your longitude
# my credentials
my_mail = "yor mail @gmail.com"
my_pass = "email pass"

# targets info
taget_address = "targer adress@gmail.com"
smptp_server = "smtp.gmail.com"
notinrange = True

#Your position is within +5 or -5 degrees of the ISS position.
def inrange():
    global iss_latitude
    global iss_longitude
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    if 30 < iss_latitude < 32 and 70 < iss_longitude < 72:
        return True


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}


# passing parameters to the sun time api to get time + converting to the local time
def sstime():
    ''''This funtion gets the sunrise and the sunset time from the Api,
    parses it to the Utc and then convets to the local time'''
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise1 = (data["results"]["sunrise"])
    sunset1 = (data["results"]["sunset"])


    # Parse times as UTC and convert to local time
    utc_offset = 5  # Pakistan Time is UTC+5
    sunrise_local = datetime.fromisoformat(sunrise1).replace(tzinfo=None) + timedelta(hours=utc_offset)
    sunset_local = datetime.fromisoformat(sunset1).replace(tzinfo=None) + timedelta(hours=utc_offset)

    time_now = datetime.now()
    global sunset, nowhour, sunrise
    nowhour = time_now.hour
    sunrise = int(str(sunrise_local).split(" ")[1].split(":")[0])
    sunset = int(str(sunset_local).split(" ")[1].split(":")[0])


# creates the msg body for the email
def msgbody():
    def dayornight():
        if sunset < nowhour < 24 and 24 > nowhour < sunrise:
            return "night"
        else:
            return "day"
    def lookornot():
        if dayornight() == "day":
            return "Look in the Sky but as its now daytime maybe you can't see it ..."
        elif dayornight() == "night":
            return "Look in the Sky as its Night Time maybe you can easily see it ..."
    subject = "ISS OverHead Look Up"
    messagebody = f"Hey Faisal\nI am delighted to tell you that the International Space Station is passing over your head \nIts {dayornight()} of the day.\n{lookornot()}"
    message = f"Subject: {subject}\n\n{messagebody}"
    return message


#  loop to check the position and sent the mail
while notinrange:
    time.sleep(60)
    if inrange():
        with smtplib.SMTP(smptp_server, 587) as connection:
            connection.starttls()
            connection.login(user=my_mail,password=my_pass)
            connection.sendmail(from_addr=my_mail,to_addrs=taget_address,msg=msgbody())
            print("mail sent")
            notinrange = False
    else:
        print(f"not in range currently its {iss_latitude},{iss_longitude}")






