from bs4 import BeautifulSoup

from work_with_book.getURL import GetURL
from work_with_book.controlWord import ControlWord
from work_with_book.bookInfo import BookInfo
from work_with_book.aboutBook import AboutBook
from work_with_book.readPage import ReadPage
from work_with_book.regexBookPages import RegexBookPages
from work_with_book.loadDataLinks import LoadDataLinks as readDataLinks


class DataCollection:

    def getData():

        foo = readDataLinks()

        links = foo.datad_books_links()

        with open('test.txt', 'w', encoding="utf8")as fr:

            for i in range(len(links)):

                getURL = GetURL()

                html_document = getURL.getHTMLdocument(links[i])

                soup = BeautifulSoup(html_document, 'html.parser')

                # Try get all page count
                control = ControlWord()

                print(control.words(soup))

                prodInfo = BookInfo()

                print(prodInfo.book_info(soup))

                readPage = ReadPage()

                print(readPage.get_page_range(soup))

                foo = RegexBookPages()

                mock_data = foo.build_book_links(

                    links[i], readPage.get_page_range(soup))

                for j in mock_data:

                    fr.write(f'{j}\n')
        fr.close()

        # about = AboutBook()
        # print(about.small_description(soup))

        # readPage = ReadPage()
        # print(readPage.read_content(soup))
