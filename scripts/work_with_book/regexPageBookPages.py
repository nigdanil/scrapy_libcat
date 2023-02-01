import re

from document import Document as readDoc


class RegexBookPages:

    doc = readDoc()

    # What we Have
    # https://libcat.ru/knigi/fantastika-i-fjentezi/alternativnaya-istoriya/385869-svetlana-shepot-galkino-schaste.html

    # Using the regex for string to find this substrings (385869-1)

    # What we need
    # https://libcat.ru/knigi/fantastika-i-fjentezi/alternativnaya-istoriya/385869-1-svetlana-shepot-galkino-schaste.html

    loadDoc = doc.load_document(r'data\oneBookLinks.txt')
    print(loadDoc)
