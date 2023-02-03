import json

from work_with_book.dataCollections import Data_Collector

from url.getURL import GetURL


class Builder:

    def data_processing(self):

        get = Data_Collector()

        builder_links = get.сrawler()
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
        with open(r'data\data.json', 'w', encoding='utf-8') as f:
            json.dump(builder_links[0], f, ensure_ascii=False, indent=4)
