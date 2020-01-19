from unittest import mock

import pytest

from tibia.crawler import Crawler
from utils import loadMockup


@pytest.fixture
def resumeHtml():
    return loadMockup("resume.html")

@mock.patch("downloader.Downloader")
def testTibiaSearchCharacter(downloader_mock, snapshot, resumeHtml):
    character = "bobo"
    url = "https://www.tibia.com"

    downloader = downloader_mock.return_value
    downloader.post.return_value = mock.Mock(text=resumeHtml)
    crawler = Crawler(url, character, downloader)

    snapshot.assert_match(crawler.getTibiaInformation(character).__dict__)
