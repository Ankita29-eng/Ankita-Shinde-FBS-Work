# Create a class Product with members as pid,pname,price and quantity.
# Add following methods:
#d.constructor (Support both parameterized and parameterless)
#e. Destructor
#f. ShowBook
class Product:
    #Parameterless Constructor
    def __init__(self,pid = 0,pname="Unknown",price = 0,quantity=0):
        self.pid =pid
        self.pname =pname
        self.price = price
        self.quantity = quantity
    # Destructor
    def __del__(self):
        print("Destructor Called")
    #ShowBook Method
    def ShowBook (self):
        print("Product ID:",self.pid)
        print("Product Name:",self.pname)
        print("Price:",self.price)
        print("Quantity:",self.quantity)

    # parameterized Constructor
p1 = Product(101,"Laptop",5000,2)

# Parameterless Constructor
p2=Product()

print("Product1:")
p1.ShowBook()

print("\nProduct2:")
p2.ShowBook()

