class ReadPage:

    def __init__(self):
        self.temp = []
        self.count = ""

    def get_page_range(self, soup):
        # xpath for get count of all pages in tag <a>
        # //div[@class = 'pages']
        self.pagenav = soup.find('div', class_='pages')

        self.count = ([1] + [int(a.text.strip())
                             for a in self.pagenav.find_all('a')])

        return self.count

    def read_content(self, soup):

        print(self.get_page_range(soup))

        arg = soup.select("p")

        for i in range(8, 100):

            if arg[i].text == "Шрифт:":
                break
            self.temp.append(arg[i].text.replace(u'\xa0', u' '))
        return self.temp
