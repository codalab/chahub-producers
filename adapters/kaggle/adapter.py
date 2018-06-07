import maya
import requests

from adapters.base_scraper import BaseScraper


class KaggleAdapter(BaseScraper):
    base_url = "https://www.kaggle.com/competitions.json?page={page}"

    def begin(self):
        # There are <30 pages currently, I don't think we'll ever hit 9999
        for page in range(1, 9999):
            response = requests.get(self.base_url.format(page=page))
            data = response.json()
            competitions = data["pagedCompetitionGroup"]["competitions"]

            # get "grouped" competitions (tagged?)
            if data["fullCompetitionGroups"]:
                for group in data["fullCompetitionGroups"]:
                    if group["competitions"]:
                        competitions += group["competitions"]

            for comp in competitions:
                print("Sending competition: ID={competitionId} Title='{competitionTitle}'".format(**comp))
                end = maya.when(comp["deadline"])
                self.send_to_chahub("competitions/", {
                    "remote_id": comp["competitionId"],
                    "title": comp["competitionTitle"].strip(),
                    "created_by": comp["organizationName"],
                    "start": comp["enabledDate"],
                    "logo": comp["thumbnailImageUrl"],
                    "url": "https://www.kaggle.com{}".format(comp["competitionUrl"]),
                    "participant_count": comp["totalTeams"],
                    "end": end.iso8601(),
                    "description": comp["competitionDescription"],
                    "html_text": None,
                    "active": maya.now() < end,
                    "prize": comp["rewardQuantity"],
                    "published": True,
                })

            # No more competitions!
            if not competitions:
                break
