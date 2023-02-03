import re


class RegexBookPages:

    def __init__(self):
        self.temp = []

    def build_book_links(self, links, arg):

        first_patern = r'^https.*/[0-9]'

        second_patern = r'\/[0-9].*\.html$'

        third_patern = r'^\/[0-9]*-'

        fourth_patern = r'^\/[0-9]*[-]{1}'

        empty_string = ''

        for i in range(arg[0], (arg[-1]+arg[0])):

            string_first_part = re.findall(first_patern, links)

            string_last_part = re.findall(second_patern, links)

            first_step = re.sub(third_patern, empty_string,
                                string_last_part[0])

            second_step = re.findall(fourth_patern, string_last_part[0])

            third_step = (second_step[0] + (f'{i}-'))

            # Build the book pages links
            self.temp.append(
                f'{string_first_part[0][:-2]}{third_step}{first_step}')

        return self.temp
