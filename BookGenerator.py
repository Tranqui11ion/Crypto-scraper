class BookGenerator():
    def __init__(self, books):
        self.books = books
        self.i = 0

    def __next__(self):
        if self.i < len(self.books):
            current = self.books[self.i]
            self.i += 1
            return current
        else:
            raise StopIteration()
