# Create a class Product with members as pid,pname,price and quantity.
# Add following methods:
#e. Constructor (Support both parameterized and parameterless)
#f. Destructor
#g.ShowBook
#h. Add static member discount
#i. Provide methods for applying discount on price of product.
class Product:
    #static member
    discount = 10  #10% discount

    # Constructor (parameterized + parameterless)
    def __init__(self,pid = None,pname = None,price =0,quantity=0):
        self.pid = pid
        self.pname =pname
        self.price = price
        self.quantity = quantity

    #Method to apply discount
    def apply_discount(self):
        discount_amount = self.price*Product.discount/100
        self.price = self.price-discount_amount

    # ShowBook method
    def ShowBook(self):
        print("Product ID:",self.pid)
        print("Product Name:",self.pname)
        print("Price:",self.price)
        print("Quantity:",self.quantity)

    # Destructor
    def __del__(self):
        print("Product Object destroyed")

    #Parameterized object
p1 = Product(101,"Laptop",5000,2)

print("Before Discount:")
p1.ShowBook()

#Apply discount
p1.apply_discount()

print("\nAfter Discount:")
p1.ShowBook()

#Parameterized object
p2 = Product()

print("\nParameterless Product:")
p2.ShowBook()
