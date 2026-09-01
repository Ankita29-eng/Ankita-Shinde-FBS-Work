# Create a class Book with members as bid ,bname, price and author.Add following methods:
#a. Constructor(support both parameterized and parameterless)
#b.Destructor
#c. ShowBook
#d. Add static variable count and also maintain count of objects created.
class Book:
    # static variable
    count = 0 

    # constructor
    def __init__(self,bid =None,bname =None,price =0,author=None):
        self.bid = bid
        self.bname = bname
        self.price = price
        self.author = author

        # Increase count whenever object is created
        Book.count += 1

    #Destructor
    def __del__(self):
        print("Book Object destroyed")

    #ShowBook method
    def ShowBook(self):
        print("Book ID:",self.bid)
        print("Book Name:",self.bname)
        print("Price:",self.price)
        print("Author:",self.author)
        print("----------")

#Parameterized object
b1 = Book(101,"python Programing",500,"john")

# Parameterless object
b2 = Book()

#Display book details
b1.ShowBook()
b2.ShowBook()

#Display total objects created
print("Total Objects created:",Book.count)