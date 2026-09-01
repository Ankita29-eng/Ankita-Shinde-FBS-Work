# Create a class Shirt with members as sid,sname,type(formal etc),price and size (small, large,etc).
# Add following methods:
#j. Constructor(Support both parameterized and parameterless)
#k.Destructor
#l.ShowBook
#m.For each size of shirt price should change by 10%.
#(eg.If 1000 is price then small price = 1000,medium = 1100,large = 1200 and xlarge = 1300)
# Use static concept
class Shirt:

    #Static variable
    price_increment = 10

    #Constructor - parameterized and parameterless
    def __init__(self,sid=None,sname =None,type =None,price =0,size=None):
        self.sid=sid
        self.sname = sname
        self.type = type
        self.price = price
        self.size = size

    #Destructor
    def __del__(self):
        print("Shirt object destroyed")

    #ShowBook method
    def ShowBook(self):
        print("Shirt ID:",self.sid)
        print("Shirt Name:",self.sname)
        print("Type:",self.type)
        #print("Price:",self.price)
        print("Size:",self.size)

    #Price according to size
        if self.size == "small":
            final_price = self.price

        elif self.size == "medium":
            final_price = self.price+(self.price*Shirt.price_increment/100)

        elif self.size == "large":
            final_price = self.price+(self.price*2*Shirt.price_increment/100)

        elif self.size == "xlarge":
            final_price = self.price+(self.price*3*Shirt.price_increment/100)

        else:
            final_price=self.price
        print("Price:",final_price)
        print('----------')

#Parameterized object
s1 = Shirt(101,"Formal Shirt","Formal",1000,"small")
s1.ShowBook()

s2=Shirt(102,"Formal Shirt","Formal",1000,"medium")
s2.ShowBook()

s3 = Shirt(103,"Formal Shirt","Formal",1000,"large")
s3.ShowBook()

s4 = Shirt(104,"FormalShirt","Formal",1000,"xlarge")
s4.ShowBook()

#Parameterless Object
s5 = Shirt()
#s5.ShowBook()