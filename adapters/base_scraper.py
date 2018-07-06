import json
import os
import requests
import traceback


CHAHUB_API_URL = os.environ.get('CHAHUB_API_URL', 'https://chahub.org/api/v1/')


class BaseScraper:

    def send_to_chahub(self, endpoint, data):
        assert self.api_key, "CHAHUB_API_KEY environment variable is required, sign up for an API Key by posting an issue " \
                             "so a Chahub admin can make one for you."

        try:
            url = "{}{}".format(CHAHUB_API_URL, endpoint)
            print("Sending competition to {api_url} with Title='{title}'".format(api_url=url, **data))
            # print("Posting data: {}".format(data))
            response = requests.post(url, json.dumps(data), headers={
                'Content-type': 'application/json',
                'X-CHAHUB-API-KEY': self.api_key,
            })

            if response.status_code not in (200, 201):
                print("ERROR posting to chahub:")
                print(response.content)
        except:
            traceback.print_exc()
