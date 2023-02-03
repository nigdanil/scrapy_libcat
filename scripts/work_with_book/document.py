class Document:

    def load_document(self, filename):

        with open(f'{filename}', 'r', encoding="utf8")as fr:

            return fr.readlines()
