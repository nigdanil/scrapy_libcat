import re

from document import Document as readDoc


class RegexBookPages:

    doc = readDoc()

    loadDoc = doc.load_document(r'data\oneBookLinks.txt')

    # Need create func what get data array
    # Mocking data array
    temp = [1, 2, 3, 4, 5, 6, 7, 272]

    for i in range(temp[0], (temp[-1]+temp[0])):

        string_first_part = re.findall(r'^https.*/[0-9]', loadDoc)

        string_last_part = re.findall(r'\/[0-9].*\.html$', loadDoc)

        a = re.sub(r'^\/[0-9]*-', '', string_last_part[0])

        b = re.findall(r'^\/[0-9]*[-]{1}', string_last_part[0])

        c = (b[0] + (f'{i}-'))
        # Build the links
        print(f'{string_first_part[0][:-2]}{c}{a}')
