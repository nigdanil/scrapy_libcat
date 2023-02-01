import re


class RegexBookPages:

    def __init__(self):
        self.temp = []

    def build_book_links(self, links, arg):

        # Mocking data array
        # self.temp = [1, 2, 3, 4, 5, 6, 7, 272]

        for i in range(arg[0], (arg[-1]+arg[0])):

            string_first_part = re.findall(r'^https.*/[0-9]', links)

            string_last_part = re.findall(r'\/[0-9].*\.html$', links)

            a = re.sub(r'^\/[0-9]*-', '', string_last_part[0])

            b = re.findall(r'^\/[0-9]*[-]{1}', string_last_part[0])

            c = (b[0] + (f'{i}-'))

            # Build the book pages links
            self.temp.append(f'{string_first_part[0][:-2]}{c}{a}')

        return self.temp
