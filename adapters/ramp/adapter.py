import requests
from lxml import html


class RampAdapter:
    base_url = "https://www.ramp.studio/problems"

    def begin(self):
        response = requests.get(self.base_url)
        page = html.fromstring(response.content)

        competition_elements = page.cssselect('li a[href^="/problems/"]')

        for comp in competition_elements:
            title = comp.text_content()
            url = "https://www.ramp.studio{}".format(comp.attrib['href'])
            pass


