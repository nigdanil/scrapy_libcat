import re
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

from document import Document as readDoc


class GetURL:

    def __init__(self):
        self.text_data = ""

    def getHTMLdocument(self, url):

        ua = UserAgent()
        header = {'User-Agent': str(ua.chrome)}

        self.text_data = requests.get(url, proxies=header)

        return self.text_data.text


doc = readDoc()
loadDoc = doc.load_document(r'src\links.txt')

getURL = GetURL()
html_document = getURL.getHTMLdocument(loadDoc)

soup = BeautifulSoup(html_document, 'html.parser')


class ControlWord:
    def ___init__(self):
        self.temp = ""

    def words(self, soup, arg):
        if soup.find_all(string=re.compile(arg)):
            self.temp = "failed"
        else:
            self.temp = "passed"
        return self.temp


class AboutBook:
    def small_description(self, soup):
        return soup.select_one(".pre").text


class ProductInfo:
    def __init__(self):
        self.temp = []

    def book_info(self, soup):

        inner_ul = soup.find('ul', class_='tg-productinfo')

        inner_items = [li.text.strip() for li in inner_ul.find_all('li')]

        for i in range(0, 6):
            self.temp.append(inner_items[i].split(":"))
        return self.temp


class ReadPage:
    def __init__(self):
        self.temp = []

    def read_content(self, arg):

        for i in range(8, 100):

            if arg[i].text == "Шрифт:":
                break
            self.temp.append(arg[i].text.replace(u'\xa0', u' '))
        return self.temp

# control = ControlWord()
# print(control.words(soup, "ознакомительный отрывок"))


about = AboutBook()
print(about.small_description(soup))
