class BookCover:

    def __init__(self):

        self.temp = []

    def book_cover(self, soup):

        tag_div = 'div'

        book_cover = 'tg-frontcover'

        temp_data = soup.find(f'{tag_div}', class_=f'{book_cover}')

        for element in temp_data:

            self.temp.append('https://libcat.ru/'+element['src'])

        return self.temp
