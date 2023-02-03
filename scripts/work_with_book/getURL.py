import requests
from fake_useragent import UserAgent


class GetURL:

    def __init__(self):

        self.temp = ''

    def getHTMLdocument(self, url):

        ua = UserAgent()

        header = {'User-Agent': str(ua.chrome)}

        self.temp = requests.get(url, proxies=header)

        return self.temp.text
