#Create a class Shirt with members as sid,sname,type(formal etc),price and size(small,large etc).
# Add following methods:
#g. Constructor(Support both parameterized and parameterless)
#h. Destructor
#i. ShowBook
class Shirt:
# Parameterized and Parameterless Constructor
    def __init__(self,sid =None,sname =None,type = None,price = 0,size =None):
        self.sid = sid
        self.sname = sname
        self.type = type
        self.price= price
        self.size = size
    # Destructor
    def __del__(self):
        print("Shirt Object destroyed")

    # ShowBook method
    def ShowBook(self):
        print("Shirt ID:",self.sid)
        print("Shirt Name:",self.sname)
        print("Shirt Type:",self.type)
        print("Price:",self.price)
        print("Size:",self.size)

#Parameterized object
s1 = Shirt(101,"peter England","Formal",1500,"Large")
s1.ShowBook()

print()

# Parameterless object
s2 = Shirt ()
s2.ShowBook()
        
