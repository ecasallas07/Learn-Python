class Book:
    def read(self):
        print("Reading book")
        return self

    def writter(self):
        print("Writter book")
        return self

    def loan(self):
        print("Loan Books")
        return self

#return selef is for call more mtehods in same inline
book_1 = Book()
book_1.read().writter()
