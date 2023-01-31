from bs4 import BeautifulSoup
from work_with_book.document import Document as readDoc
from work_with_book.getURL import GetURL
from work_with_book.controlWord import ControlWord
from work_with_book.productInfo import ProductInfo
from work_with_book.aboutBook import AboutBook
from work_with_book.readPage import ReadPage


doc = readDoc()
loadDoc = doc.load_document(r'data\oneBookLinks.txt')

getURL = GetURL()
html_document = getURL.getHTMLdocument(loadDoc)

soup = BeautifulSoup(html_document, 'html.parser')

# control = ControlWord()
# print(control.words(soup, "ознакомительный отрывок"))

# prodInfo = ProductInfo()
# print(prodInfo.book_info(soup))

about = AboutBook()
print(about.small_description(soup))

# Must Fix bug, can remember what argument must give in function=)
# readPage = ReadPage()
# print(readPage.read_content(soup))
