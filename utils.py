import unicodedata

def normalizeText(text: str) -> str:
    return unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("utf-8")

def loadMockup(mockup_name: str, encoding="utf-8"):
    with open(f"tests/mockup/{mockup_name}", encoding=encoding, mode="r") as f:
        return f.read()