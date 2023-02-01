class Document:

    def load_document(self, filename):

        with open(filename, 'r', encoding="utf8")as fr:

            return fr.readlines()
