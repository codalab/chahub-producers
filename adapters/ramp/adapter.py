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

            self.send_to_chahub("competitions/", {
                "title": comp.text_content(),
                "url": "https://www.ramp.studio{}".format(comp.attrib['href']),
                "participant_count": participant_count,
                "html_text": None,
                "active": True,
                "published": True,
            })
