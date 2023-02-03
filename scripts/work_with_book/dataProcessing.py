import logging
import json
from bs4 import BeautifulSoup


from work_with_book.readPage import ReadPage
from work_with_book.dataCollections import Data_Collector

from url.getURL import GetURL


class Builder:

    def __init__(self):
        self.temp_data_pages = []

    def data_processing(self):

        temp_readData = []
        temp = []

        logging.basicConfig(filename='Debug.log',
                            encoding='utf-8', level=logging.INFO)

        get = Data_Collector()

        builder_links = get.сrawler()
        # Importen! [1] is all links array
        # Must do [1][0] - one books links
        temp_readData = builder_links[1]

        for first_iter in range(len(temp_readData)):

            with open(f'data\data_{first_iter}.json', 'w', encoding='utf-8') as f:
                # Second iteration
                # First iteration

                for second_iter in range(len(temp_readData[first_iter])):

                    print(second_iter)
                    # self.temp.append(temp_readData[first_iter][second_iter])

                    getURL = GetURL()

                    foo = ReadPage()

                    html_document = getURL.getHTMLdocument(
                        temp_readData[first_iter][second_iter])

                    soup = BeautifulSoup(html_document, 'html.parser')

                    temp.insert(
                        first_iter, foo.read_content(soup))

                json.dump(temp, f,
                          ensure_ascii=False, indent=4)

                temp.clear()

        #     break

        # Need refactoring code for JSON format
        # self.Books[i] = {

        #     'book_ID': i,
        #     'prodInfo': self.prodInfo.book_info(soup),
        #     'about': self.about.small_description(soup),
        #     'pageCount': self.readPage.get_page_range(soup)[-1],
        #     # 'book_pages': book_pages[i]

        # }

        # class ReadPage:
        # Function read text from page in book
        # def read_content(self, soup):

        # Take links for all pages 1 book
        # readData[0]
        # Take links for all pages all books
        # readData
        # with open(r'data\data.json', 'w', encoding='utf-8') as f:
        #     json.dump(self.temp_data_pages, f, ensure_ascii=False, indent=4)
