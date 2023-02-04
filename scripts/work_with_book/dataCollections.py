from bs4 import BeautifulSoup

from url.getURL import GetURL
from work_with_book.controlWord import ControlWord
from work_with_book.bookInfo import BookInfo
from work_with_book.aboutBook import AboutBook
from work_with_book.readPage import ReadPage
from work_with_book.regexBookPages import RegexBookPages
from work_with_book.loadDataLinks import LoadDataLinks as readDataLinks
from work_with_book.bookCover import BookCover


class Data_Collector:

    def __init__(self):

        self.book_pages = []

        self.books_info_part_1 = []

        self.books_info_part_2 = []

        self.books_info_part_3 = []

        self.booksCovers = []

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

                dataBooksCover = BookCover()

                prodInfo = BookInfo()

                about = AboutBook()

                readPage = ReadPage()

                builder_links = RegexBookPages()

                readPage = ReadPage()

                # Pages links generator
                self.book_pages.append(builder_links.build_book_links(
                    links[i], readPage.get_page_range(soup)))

                self.booksCovers.append(dataBooksCover.book_cover(soup))

                self.books_info_part_1.append(prodInfo.book_info(soup))

                self.books_info_part_2.append(about.small_description(soup))

                self.books_info_part_3.append(
                    readPage.get_page_range(soup)[-1])

        return self.books_info_part_1, self.books_info_part_2, self.books_info_part_3, self.book_pages, self.booksCovers
