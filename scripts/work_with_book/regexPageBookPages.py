import re

from document import Document as readDoc
from readPage import ReadPage


class RegexBookPages:

    doc = readDoc()

    # What we Have
    # https://libcat.ru/knigi/fantastika-i-fjentezi/alternativnaya-istoriya/385869-svetlana-shepot-galkino-schaste.html

    # Using the regex for string to find this substrings (385869-1)

    # What we need
    # https://libcat.ru/knigi/fantastika-i-fjentezi/alternativnaya-istoriya/385869-1-svetlana-shepot-galkino-schaste.html

    loadDoc = doc.load_document(r'data\oneBookLinks.txt')

    # Read page count
    # readPage = ReadPage()
    # print(readPage.read_content(soup))

    # Need create func what get data array
    # Mocking data array
    temp = [1, 2, 3, 4, 5, 6, 7, 100]
    res = [temp[0], temp[-1]]

    print(res)

    for i in range(res[0], res[1]):

        string_first_part = re.findall(r'^https.*/[0-9]', loadDoc)

        string_last_part = re.findall(r'\/[0-9].*\.html$', loadDoc)

        a = re.sub(r'^\/[0-9]*-', '', string_last_part[0])

        b = re.findall(r'^\/[0-9]*[-]{1}', string_last_part[0])

        c = (b[0] + (f'{i}-'))
        # Build the links
        print(f'{string_first_part[0][:-2]}{c}{a}')
