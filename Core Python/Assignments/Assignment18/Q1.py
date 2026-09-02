#1. Create a class Complex Number with data members as real and imag and add following methods:
#a.Constructor
#b.Destructor
#c.Overload +,-operator
class ComplexNumber:
    #Constructor
    def __init__(self,real=0,imag=0):
        self.real = real
        self.imag = imag

    #Overload + operator
    def __add__(self, other):
        return ComplexNumber(self.real+other.real,self.imag+other.imag)

    # Overload - operator
    def __sub__(self, other):
        return ComplexNumber(self.real-other.real,self.imag-other.imag)

    # Display
    def __str__(self):
        return f"{self.real}+{self.imag}i"
    
    #Destructor
    def __del__(self):
        print("Complex Number object destroyed")

# Creating objects
c1=ComplexNumber(10,20)
c2=ComplexNumber(5,10)

print("First Complex Number:",c1)
print("Second Complex Number:",c2)

#Addition
c3 = c1+c2
print("Addition:",c3)

#Substraction
c4=c1-c2
print("Substraction:",c4)
