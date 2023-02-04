import logging
import json
from bs4 import BeautifulSoup


from work_with_book.readPage import ReadPage
from work_with_book.dataCollections import Data_Collector

from url.getURL import GetURL


class Builder:

    def data_processing(self) -> None:

        temp_readData = []

        temp = []

        Books = {}

        get = Data_Collector()

        builder_links = get.сrawler()

        temp_bookInfo = builder_links[0]

        temp_readData = builder_links[1]

        temp_booksCovers = builder_links[2]

        prodInfo = 1

        about = 2

        pageCount = 3

        # First iteration
        for first_iter in range(len(temp_readData)):

            Books = {

                'bookID': first_iter,

                'prodInfo': temp_bookInfo[first_iter+prodInfo],

                'bookCover': temp_booksCovers[first_iter],

                'about': temp_bookInfo[first_iter+about],

                'pageCount': temp_bookInfo[first_iter+pageCount]
            }

            with open(f'data\data_{first_iter}.json', 'w', encoding='utf-8') as f:

                # Second iteration
                for second_iter in range(len(temp_readData[first_iter])):

                    print(second_iter)

                    getURL = GetURL()

                    foo = ReadPage()

                    html_document = getURL.getHTMLdocument(
                        temp_readData[first_iter][second_iter])

                    soup = BeautifulSoup(html_document, 'html.parser')

                    temp.append(foo.read_content(soup))

                keys = range(temp_bookInfo[first_iter+pageCount])

                # Convert list to dect
                for i in keys:

                    Books[i] = temp[i]

                json.dump(Books, f,
                          ensure_ascii=False, indent=4)

            f.close()

            prodInfo += pageCount

            about += pageCount

            pageCount += pageCount

            temp.clear()

            Books.clear()
