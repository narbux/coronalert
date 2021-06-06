import requests
import logging

logger = logging.getLogger(__name__)

class PushMessage():
    """Send a pushmessage through a Gotify-server.
    Prerequisites:
        - Gotify server (https://gotify.net/)
        - An API-key
    
    @param url: str to a Gotify-server (no trailing slash)
    @param key: str to authenticate REST API-call
    """

    def __init__(self, url: str, key: str):
        self.url = url
        self.key = key

    def post_msg(self, title: str, message: str, priority: int):
        """
        @param title: Title of the push message
        @param message: Contents of the push message
        @param priority: Integer between 0 and 11. Higher is more
                        priority for the notification on Android
        """

        headers = {
            "X-GOTIFY-KEY" : self.key,
            "Content-Type" : 'application/json'
        }

        payload = {
            "title" : title,
            "message" : message,
            "priority" : priority
        }

        r = requests.post(self.url + "/message", headers=headers, json=payload)
        
        if r.status_code == 200:
            logger.debug(r.text)
            return True
        else:
            logger.error(f"Request response: {r.status_code}; {r.text}")
            return False