import requests

class Downloader:
    def __init__(self):
        self.session = requests.Session()

    def get(self, url, params=None):
        response = self.session.get(url, params=params, verify=False)
        response.raise_for_status
        return response

    def post(self, url, data=None):
        response = self.session.post(url, data=data, verify=False)
        response.raise_for_status
        return response

    def close(self):
        self.session.close()