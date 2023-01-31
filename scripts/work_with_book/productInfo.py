class ProductInfo:
    def __init__(self):
        self.temp = []

    def book_info(self, soup):

        inner_ul = soup.find('ul', class_='tg-productinfo')

        inner_items = [li.text.strip() for li in inner_ul.find_all('li')]

        for i in range(0, 6):
            self.temp.append(inner_items[i].split(":"))
        return self.temp
