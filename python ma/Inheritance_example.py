class BookStore:
    def __init__(self,b1,b2):
        self.b1=input('Enter a book name:')
        self.b2=input('Enter a book name:')
  
    def Book(bk):
        print(bk.b1)
        print(bk.b2)

# z=BookStore('b1','b2')
# z.Book()

class Category(BookStore):
    def __init__(self, b1, b2,b3,b4,b5):
        super().__init__(b1, b2)
        self.b3=input('Enter a book name:')
        self.b4=input('Enter a book name:')
        self.b5=input('Enter a book name:')

    def CBook(cb):
        print(cb.b1)
        print(cb.b2)
        print(cb.b3)
        print(cb.b4)
        print(cb.b5)

y=Category('b1','b2','b3','b4','b5')
y.CBook()