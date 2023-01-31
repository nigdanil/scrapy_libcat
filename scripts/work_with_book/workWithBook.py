from bs4 import BeautifulSoup

from work_with_book.document import Document as readDoc
from work_with_book.getURL import GetURL
from work_with_book.controlWord import ControlWord
from work_with_book.productInfo import ProductInfo
from work_with_book.aboutBook import AboutBook
from work_with_book.readPage import ReadPage


class DataCollection:

    def getData():

        doc = readDoc()
        loadDoc = doc.load_document(r'data\oneBookLinks.txt')

        getURL = GetURL()
        html_document = getURL.getHTMLdocument(loadDoc)

        soup = BeautifulSoup(html_document, 'html.parser')

        control = ControlWord()
        print(control.words(soup))

        prodInfo = ProductInfo()
        print(prodInfo.book_info(soup))

        about = AboutBook()
        print(about.small_description(soup))

        readPage = ReadPage()
        print(readPage.read_content(soup))
