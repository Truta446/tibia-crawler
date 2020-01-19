import json
from urllib.parse import urljoin

from tibia.parser import Parser


class Crawler:
    def __init__(self, tibia_url, character, downloader):
        self.tibia_url = tibia_url
        self.downloader = downloader
        self.parser = Parser()
        self.getTibiaInformation(character)

    def getTibiaInformation(self, character):
        character_url = urljoin(self.tibia_url, "community/?subtopic=characters")
        params = self.configParams(character)
        response = self.downloader.post(character_url, data=params)
        
        if self.parser.characterNotFound(response.text):
            parsed = self.parser.parse(response.text)
            self.saveData(parsed.__dict__)
            return parsed

    def configParams(self, character):
        return {"name": character, "Submit.x": 0, "Submit.y": 0}

    def saveData(self, data):
        name = data.get("name").lower().replace(" ", "_")

        with open(f"tibia/database/{name}.json", "w", encoding="utf-8") as f:
            json.dump(data, f)
            print(f"Personagem {name} foi salvo com sucesso!")