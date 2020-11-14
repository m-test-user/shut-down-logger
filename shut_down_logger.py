import datetime
import logging
import os
import time

import requests
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()

URL = os.getenv('URL')
response_status = ''
err_counter = 0
err_log_timeout = 121
requests_timeout = 3

def response_get(response_status):

    try:
        response = requests.get(URL)
        response_status = str(response.ok)
    except:
        response_status = 'Not available'
    finally:
        return response_status
    

def response_log(err_counter, response_status):
    logging.basicConfig(level = logging.INFO, filename = "log.txt")

    if response_status == 'Not available':
        logging.error\
            (f'({datetime.datetime.today()}) {response_status}: {URL}')
        err_counter = err_counter + 1

    return err_counter 


def message_push(err_counter):

    TWILIO_ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')
    TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

    if err_counter == 1:

        client.messages.create(
            body = str(os.getenv('body_message') + f': {URL}'),
            from_ = str(os.getenv('from_number')),
            to = str(os.getenv('to_number')),
            )

    return err_counter


if __name__ == '__main__':

    while True:

        err_counter = message_push(response_log\
            (err_counter, response_get(response_status)))
        
        if err_counter >= err_log_timeout or response_status == 'True':
            err_counter = 0
        
        time.sleep(requests_timeout)
