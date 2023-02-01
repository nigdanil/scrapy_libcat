import re


class ControlWord:

    def ___init__(self):

        self.temp = ""

    def words(self, soup):

        brake_word = "ознакомительный отрывок"

        find_tag = "failed"

        not_find_tag = "passed"

        if soup.find_all(string=re.compile(f'{brake_word}')):

            self.temp = f'{find_tag}'

        else:

            self.temp = f'{not_find_tag}'

        return self.temp
