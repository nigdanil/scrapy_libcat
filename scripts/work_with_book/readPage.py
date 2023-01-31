class ReadPage:
    def __init__(self):
        self.temp = []

    def read_content(self, soup):

        arg = soup.select("p")

        for i in range(8, 100):

            if arg[i].text == "Шрифт:":
                break
            self.temp.append(arg[i].text.replace(u'\xa0', u' '))
        return self.temp
