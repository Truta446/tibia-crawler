import re

from bs4 import BeautifulSoup

from model import Tibia
from utils import normalizeText

ACCOUNT_STATUS_REGEX = r"(Account\sStatus\:)"
GUILD_MEMBERSHIP_REGEX = r"(Guild\sMembership\:)"

class Parser:
    def parse(self, html):
        parsed = BeautifulSoup(html, "html.parser")
        return Tibia(
            name=self.extract_name(parsed),
            title=self.extract_title(parsed),
            sex=self.extract_sex(parsed),
            vocation=self.extract_vocation(parsed),
            level=self.extract_level(parsed),
            achivement=self.extract_achivement(parsed),
            world=self.extract_world(parsed),
            residence=self.extract_residence(parsed),
            guild_membership=self.extract_guild_membership(parsed),
            last_login=self.extract_last_login(parsed),
            account_status=self.extract_account_status(parsed),
            deaths=self.extract_deaths(parsed),
        )

    def extract_deaths(self, html):
        text = html.find("b", string="Character Deaths")
        if text:
            result = []
            rows = text.find_all_next("tr")

            for item in rows:
                if item.text == "Search Character" or item.text == "Account Information":
                    break

                timestamp = normalizeText(
                    item.select_one("td:nth-of-type(1)").text.strip()
                )

                description = normalizeText(
                    item.select_one("td:nth-of-type(2)").text.strip()
                )

                result.append({
                    "timestamp": timestamp,
                    "description": description
                })
            return result

    def extract_account_status(self, html):
        result = html.find("td", string=re.compile(ACCOUNT_STATUS_REGEX))
        return self._getInformation(result)

    def extract_last_login(self, html):
        result = html.find("td", string="Last Login:")
        return normalizeText(self._getInformation(result))

    def extract_guild_membership(self, html):
        result = html.find("td", string=re.compile(GUILD_MEMBERSHIP_REGEX))
        return normalizeText(self._getInformation(result))

    def extract_residence(self, html):
        result = html.find("td", string="Residence:")
        return self._getInformation(result)

    def extract_world(self, html):
        result = html.find("td", string="World:")
        return self._getInformation(result)

    def extract_achivement(self, html):
        result = html.find("td", string="Achievement Points:")
        return self._getInformation(result)

    def extract_level(self, html):
        result = html.find("td", string="Level:")
        return self._getInformation(result)

    def extract_vocation(self, html):
        result = html.find("td", string="Vocation:")
        return self._getInformation(result)

    def extract_sex(self, html):
        result = html.find("td", string="Sex:")
        return self._getInformation(result)

    def extract_title(self, html):
        result = html.find("td", string="Title:")
        return self._getInformation(result)
    
    def extract_name(self, html):
        result = html.find("td", string="Name:")
        return self._getInformation(result)

    def characterNotFound(self, html):
        parsed = BeautifulSoup(html, "html.parser")
        result = parsed.find(string=re.compile(r"(does\snot\sexist.)"))
        return not bool(result)

    def _getInformation(self, result):
        if result:
            return result.find_next("td").text.strip()
