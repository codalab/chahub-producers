import json
import os
from time import sleep

import requests
import traceback


CHAHUB_API_URL = os.environ.get('CHAHUB_API_URL', 'https://chahub.org/api/v1/')
CHAHUB_DEBUG = os.environ.get('CHAHUB_DEBUG', False)


class BaseScraper:

    def send_to_chahub(self, endpoint, data):
        assert self.api_key, "CHAHUB_API_KEY environment variable is required, sign up for an API Key by posting an issue " \
                             "so a Chahub admin can make one for you."

        try:
            url = "{}{}".format(CHAHUB_API_URL, endpoint)
            print(f"{self.__class__.__name__} :: Sending {len(data)} {endpoint} to {CHAHUB_API_URL}")

            if 'competitions' in endpoint:
                print("Competition titles:")
                for index, competition in enumerate(data):
                    print(f"{index + 1}. {competition.get('title')}")

            if CHAHUB_DEBUG:
                print("[DEBUG] Posting data: {}".format(data))

            response = requests.post(url, json.dumps(data), headers={
                'Content-type': 'application/json',
                'X-CHAHUB-API-KEY': self.api_key,
            })

            if response.status_code not in (200, 201):
                print("ERROR posting to chahub:")
                print(response.content)
        except:
            traceback.print_exc()

        # One second sleep between sends, so we don't overwhelm Chahub. These scrapers are only ran
        # once per day so this shouldn't be too impactful
        sleep(1)
