# Create a class Book with members as bid,bname,price and author. Add following methods:
#a. Constructor (Support both parameterized and parameterless)
#b.Destructor
#c.ShowBook
class Book:
    # Constructor
    def __init__(self,bid=0,bname ="",price=0.0,author=""):
        self.bid = bid
        self.bname = bname
        self.price = price
        self.author = author
    # Destructor
    def __del__(self):
        print("Book object destroyed")

    # ShowBook method
    def ShowBook (self):
        print("Book ID:",self.bid)
        print("Book Name:",self.bname)
        print("Price:",self.price)
        print("Author:",self.author)

# Parameterless constructor
b1 = Book()
b1.ShowBook()
print("---------------")

# Parameterized Constructor
b2 = Book (101,"Python Programming",500,"John")
b2.ShowBook()
