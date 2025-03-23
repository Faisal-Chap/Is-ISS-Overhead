# ISS Overhead Notifier

## Overview
This Python script notifies you via email when the International Space Station (ISS) is overhead your location. It continuously checks the ISS position and sends an email when the ISS is within a specified range. Additionally, it considers local sunrise and sunset times to inform you whether the ISS is visible in the night sky.

## Features
- Retrieves real-time ISS position using the Open Notify API.
- Fetches local sunrise and sunset times from the Sunrise-Sunset API.
- Determines if the ISS is within a specified latitude and longitude range.
- Sends an email notification when the ISS is overhead.
- Runs in a loop to check periodically every 60 seconds.

## Requirements
- Python 3.x
- `requests` library
- `smtplib` library

## Installation
1. Clone this repository or download the script.
2. Install dependencies:
   ```sh
   pip install requests
   ```
3. Set up your email credentials and location details in the script:
   ```python
   MY_LAT = 31.996754  # Your latitude
   MY_LONG = 71.178692  # Your longitude
   my_mail = "your_email@gmail.com"
   my_pass = "your_email_password"
   target_address = "target_email@gmail.com"
   smtp_server = "smtp.gmail.com"
   ```
4. Ensure you have enabled "Less Secure Apps" access in your email account settings (for Gmail users) or generate an app password.

## Usage
Run the script using:
```sh
python iss_notifier.py
```
The script will:
1. Fetch the ISS location and your local sunrise/sunset times.
2. Check if the ISS is within ±1° of your latitude and longitude.
3. If the ISS is overhead, it will send you an email notification.
4. The script runs in a loop, checking the ISS position every 60 seconds.

## Customization
- Modify the latitude and longitude values to match your location.
- Adjust the email content in the `msgbody()` function.
- Change the loop frequency by modifying `time.sleep(60)`.

## API References
- [Open Notify ISS API](http://open-notify.org/Open-Notify-API/)
- [Sunrise-Sunset API](https://sunrise-sunset.org/api)

## Disclaimer
This script is for educational purposes only. Ensure you use secure methods for handling email credentials.

