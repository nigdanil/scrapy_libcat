from bs4 import BeautifulSoup

from work_with_book.getURL import GetURL
from work_with_book.controlWord import ControlWord
from work_with_book.bookInfo import BookInfo
from work_with_book.aboutBook import AboutBook
from work_with_book.readPage import ReadPage
from work_with_book.regexBookPages import RegexBookPages
from work_with_book.loadDataLinks import LoadDataLinks as readDataLinks


class Data_Collector:

    def __init__(self):
        self.book_pages = []
        self.books_info = []

    def сrawler(self):

        control_word = 'passed'

        readData = readDataLinks()

        links = readData.datad_books_links()

        for i in range(len(links)):

            getURL = GetURL()

            html_document = getURL.getHTMLdocument(links[i])

            soup = BeautifulSoup(html_document, 'html.parser')

            control = ControlWord()

            # Create structure
            if (control.words(soup)) == control_word:

                prodInfo = BookInfo()

                about = AboutBook()

                readPage = ReadPage()

                builder_links = RegexBookPages()

                readPage = ReadPage()

                # Pages links generator
                self.book_pages.append(builder_links.build_book_links(
                    links[i], readPage.get_page_range(soup)))

                self.books_info.append(i)

                self.books_info.append(prodInfo.book_info(soup))

                self.books_info.append(about.small_description(soup))

                self.books_info.append(readPage.get_page_range(soup)[-1])

        return self.books_info, self.book_pages
