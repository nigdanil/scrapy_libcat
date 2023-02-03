class ReadPage:

    def __init__(self):

        self.temp = []

        self.count = ''

    def get_page_range(self, soup):

        pagination_tag_div = 'div'

        pagination_class = 'pages'

        get_tag_a = 'a'

        pagenav = soup.find(
            f'{pagination_tag_div}', class_=f'{pagination_class}')

        self.count = ([1] + [int(a.text.strip())
                             for a in pagenav.find_all(f'{get_tag_a}')])

        return self.count

    def read_content(self, soup):

        reading_text_tag_p = 'p'

        block_read_start = 8

        block_read_end = 100

        read_end_control_word = 'Шрифт:'

        arg = soup.select(f'{reading_text_tag_p}')

        find_space_char = u"\xa0"

        replace_space_char = u" "

        for i in range(block_read_start, block_read_end):

            if arg[i].text == read_end_control_word:
                break

            self.temp.append(arg[i].text.replace(
                f'{find_space_char}',
                f'{replace_space_char}'))

        return self.temp
