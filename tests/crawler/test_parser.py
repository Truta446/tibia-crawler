import pytest
from bs4 import BeautifulSoup

from tibia.parser import Parser
from utils import loadMockup


@pytest.fixture
def resumeHtml():
    return loadMockup("resume.html")

@pytest.fixture
def notFoundHtml():
    return loadMockup("not_found.html")

def testExtractName(snapshot, resumeHtml):
    parsed = BeautifulSoup(resumeHtml, "html.parser")
    text = Parser().extract_name(parsed)
    snapshot.assert_match(text)

def testExtractTitle(snapshot, resumeHtml):
    parsed = BeautifulSoup(resumeHtml, "html.parser")
    text = Parser().extract_title(parsed)
    snapshot.assert_match(text)

def testExtractSex(snapshot, resumeHtml):
    parsed = BeautifulSoup(resumeHtml, "html.parser")
    text = Parser().extract_sex(parsed)
    snapshot.assert_match(text)

def testExtractVocation(snapshot, resumeHtml):
    parsed = BeautifulSoup(resumeHtml, "html.parser")
    text = Parser().extract_vocation(parsed)
    snapshot.assert_match(text)

def testExtractLevel(snapshot, resumeHtml):
    parsed = BeautifulSoup(resumeHtml, "html.parser")
    text = Parser().extract_level(parsed)
    snapshot.assert_match(text)

def testExtractAchivements(snapshot, resumeHtml):
    parsed = BeautifulSoup(resumeHtml, "html.parser")
    text = Parser().extract_achivement(parsed)
    snapshot.assert_match(text)

def testExtractWorld(snapshot, resumeHtml):
    parsed = BeautifulSoup(resumeHtml, "html.parser")
    text = Parser().extract_world(parsed)
    snapshot.assert_match(text)

def testExtractResidence(snapshot, resumeHtml):
    parsed = BeautifulSoup(resumeHtml, "html.parser")
    text = Parser().extract_residence(parsed)
    snapshot.assert_match(text)

def testExtractGuildMembership(snapshot, resumeHtml):
    parsed = BeautifulSoup(resumeHtml, "html.parser")
    text = Parser().extract_guild_membership(parsed)
    snapshot.assert_match(text)

def testExtractLastLogin(snapshot, resumeHtml):
    parsed = BeautifulSoup(resumeHtml, "html.parser")
    text = Parser().extract_last_login(parsed)
    snapshot.assert_match(text)

def testExtractAccountStatus(snapshot, resumeHtml):
    parsed = BeautifulSoup(resumeHtml, "html.parser")
    text = Parser().extract_account_status(parsed)
    snapshot.assert_match(text)

def testExtractDeaths(snapshot, resumeHtml):
    parsed = BeautifulSoup(resumeHtml, "html.parser")
    deaths = Parser().extract_deaths(parsed)
    for death in deaths:
        snapshot.assert_match(death)

def testNotFound(snapshot, notFoundHtml):
    confirmation = Parser().characterNotFound(notFoundHtml)
    assert not confirmation == True