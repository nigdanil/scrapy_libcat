class BookInfo:

    def __init__(self):

        self.temp = []

    def book_info(self, soup):

        first_tag_li = 0

        last_tag_li = 6

        splite_char = ':'

        ul_tag = 'ul'

        li_tag = 'li'

        book_info_tag = 'tg-productinfo'

        inner_ul = soup.find(f'{ul_tag}', class_=f'{book_info_tag}')

        inner_items = [li.text.strip()
                       for li in inner_ul.find_all(f'{li_tag}')]

        for i in range(first_tag_li, last_tag_li):

            self.temp.append(inner_items[i].split(f'{splite_char}'))

        return self.temp
