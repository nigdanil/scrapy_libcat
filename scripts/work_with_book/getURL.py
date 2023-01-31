import requests
from fake_useragent import UserAgent


class GetURL:

    def __init__(self):
        self.text_data = ""

    def getHTMLdocument(self, url):

        ua = UserAgent()
        header = {'User-Agent': str(ua.chrome)}

        self.text_data = requests.get(url, proxies=header)

        return self.text_data.text
