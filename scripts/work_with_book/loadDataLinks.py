from work_with_book.document import Document as readDoc


class LoadDataLinks:

    def datad_books_links(self):

        self.doc = readDoc()

        return self.doc.load_document(r'data\oneBookLinks.txt')
