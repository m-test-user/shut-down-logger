# Shut Down Logger

## About

This is a python script that checks the availability of a web service (interval 60sec) and send SMS (by [Twilio](https://www.twilio.com)) in case of a shutdown.

## Installation

1. Clon this repo


2. Run install.py and to fill in the fields:
  ```
  TWILIO_ACCOUNT_SID = 
  TWILIO_AUTH_TOKEN = 
  URL = 
  body_message = 
  from_number = 
  to_number = 
  ```
  
  
3. Run shut_down_logger.py
