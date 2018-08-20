import os
import re
import requests

from lxml import html

from adapters.base_scraper import BaseScraper


class RampAdapter(BaseScraper):
    base_url = "https://www.ramp.studio/problems"
    api_key = os.environ.get('CHAHUB_API_KEY_RAMP')

    def begin(self):
        response = requests.get(self.base_url)
        page = html.fromstring(response.content)

        competition_elements = page.cssselect('li a[href^="/problems/"]')

        print("Found {} competitions".format(len(competition_elements)))

        competitions = []

        for comp in competition_elements:
            competition_entry_text = comp.getparent().text_content()
            participant_text = re.findall('number of participants = (\d+)', competition_entry_text, re.DOTALL)

            try:
                participant_count = sum([int(n) for n in participant_text])
            except TypeError:
                participant_count = 0

            # We'll maybe use this submission count later
            # submission_text = re.findall('number of submissions = (\d+)', competition_entry_text, re.DOTALL)
            # submission_count = sum([int(n) for n in submission_text])

            url = "https://www.ramp.studio{}".format(comp.attrib['href'])

            competitions.append({
                # For RAMP we'll use the URL path as the 'remote_id':
                #    https://www.ramp.studio/problems/storm_forecast -> `storm_forecast` is the remote_id
                "remote_id": os.path.basename(url),
                "title": comp.text_content(),
                "url": url,
                "participant_count": participant_count,
                "html_text": None,
                "active": True,
                "published": True,
            })
        self.send_to_chahub("competitions/", competitions)
