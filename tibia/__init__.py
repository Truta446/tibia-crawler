from downloader import Downloader
from tibia.crawler import Crawler

class Character(Crawler):
    def __init__(self, character):
        super().__init__("https://www.tibia.com", character, Downloader())