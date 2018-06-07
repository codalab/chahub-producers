import json
import os
import requests
import traceback


CHAHUB_API_URL = os.environ.get('CHAHUB_API_URL', 'https://chahub.org/')
CHAHUB_API_KEY = os.environ.get('CHAHUB_API_KEY')

assert CHAHUB_API_KEY, "CHAHUB_API_KEY environment variable is required, sign up for an API Key by posting an issue " \
                       "so a Chahub admin can make one for you."


class BaseScraper:

    def send_to_chahub(self, endpoint, data):
        try:
            url = "{}{}".format(CHAHUB_API_URL, endpoint)
            response = requests.post(url, json.dumps(data), headers={
                'Content-type': 'application/json',
                'X-CHAHUB-API-KEY': CHAHUB_API_KEY,
            })

            if response.status_code not in (200, 201):
                print("ERROR posting to chahub:")
                print(response.content)
        except requests.ConnectionError:
            traceback.print_exc()
