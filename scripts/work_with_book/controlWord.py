import re


class ControlWord:

    def ___init__(self):

        self.temp = ""

    def words(self, soup):

        arg = "ознакомительный отрывок"

        if soup.find_all(string=re.compile(arg)):

            self.temp = "failed"

        else:

            self.temp = "passed"

        return self.temp
