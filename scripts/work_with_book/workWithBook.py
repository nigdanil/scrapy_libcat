from bs4 import BeautifulSoup

from work_with_book.getURL import GetURL
from work_with_book.controlWord import ControlWord
from work_with_book.productInfo import ProductInfo
from work_with_book.aboutBook import AboutBook
from work_with_book.readPage import ReadPage
from work_with_book.regexBookPages import RegexBookPages
from work_with_book.loadDataLinks import LoadDataLinks as readDataLinks


class DataCollection:

    def getData():

        zoo = readDataLinks()

        links = zoo.datad_books_links()

        with open('test.txt', 'w', encoding="utf8")as fr:

            for a in range(len(links)):

                getURL = GetURL()

                html_document = getURL.getHTMLdocument(links[a])

                soup = BeautifulSoup(html_document, 'html.parser')

                # Try get all page count
                control = ControlWord()

                print(control.words(soup))

                prodInfo = ProductInfo()

                print(prodInfo.book_info(soup))

                readPage = ReadPage()

                print(readPage.get_page_range(soup))

                foo = RegexBookPages()

                mock_data = foo.build_book_links(

                    links[a], readPage.get_page_range(soup))

                for i in mock_data:

                    fr.write(f'{i}\n')
        fr.close()

        # about = AboutBook()
        # print(about.small_description(soup))

        # readPage = ReadPage()
        # print(readPage.read_content(soup))
