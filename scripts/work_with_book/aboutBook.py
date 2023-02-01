class AboutBook:

    def small_description(self, soup):

        return soup.select_one(".pre").text
