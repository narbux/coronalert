import os
import requests
import logging
from dotenv import load_dotenv
from time import sleep
from pushnotify import PushMessage

load_dotenv()

YEARS = os.environ.get('YEARS').split(',')
YEARS.sort()
URL = "https://user-api.coronatest.nl/vaccinatie/programma/bepaalbaar/YEAR/NEE/NEE"
GOTIFY_KEY = os.environ.get("GOTIFY_KEY")
GOTIFY_URL = os.environ.get("GOTIFY_URL")

def send_push_message(year: int):
    msg_title= "Corona vaccination available!"
    msg_content = f"The Coronatest for {str(year)} is available!"
    push = PushMessage(GOTIFY_URL, GOTIFY_KEY)
    push.post_msg(msg_title, msg_content, 10)
    logger.info(f"Year {str(year)} available, notification send ")

def main():
    for year in YEARS:
        r_URL = URL.replace("YEAR", str(year))
        logger.debug(f"Trying {r_URL} for year {str(year)}")
        response = requests.get(r_URL)
        if response.status_code == 200:
            data = response.json()
            logger.debug(f"Response JSON: {data}")
            if data['success'] == True:
                send_push_message(year)                
                # Remove first item from sorted YEARS-list to prevent sending
                # of multiple notifications
                YEARS.pop(0) 
            else:
                logger.info(f"Year {str(year)} not available")
        else:
            logger.error(response.status_code, response.text)

if __name__ == "__main__":
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    ch = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    try:
        while True:
            logger.info("Starting program")
            main()
            sleep(120)
    except KeyboardInterrupt:
        logger.info("Exiting program")

