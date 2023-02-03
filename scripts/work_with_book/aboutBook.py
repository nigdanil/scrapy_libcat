class AboutBook:

    def small_description(self, soup):
        tag_pre = '.pre'
        return soup.select_one(f'{tag_pre}').text
