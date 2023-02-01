import re


class ControlWord:

    def ___init__(self):

        self.temp = ""

    def words(self, soup):

        brake_word = "ознакомительный отрывок"

        find_brake_word = "failed"

        not_find_brake_word = "passed"

        if soup.find_all(string=re.compile(f'{brake_word}')):

            self.temp = f'{find_brake_word}'

        else:

            self.temp = f'{not_find_brake_word}'

        return self.temp
