# Create a class Distance with data members as km,m and cm and add following methods:
#a. Constructor
#b.Destructor
#c.Overload+,-operator
class Distance:
    # Constructor
    def __init__(self,km=0,m=0,cm=0):
        self.km=km
        self.m=m
        self.cm=cm

    # Overload + operator
    def __add__(self, other):
        total_cm=(self.km * 100000+self.m*100+self.cm)+\
            (other.km*100000+other.m*100+other.cm)
        km= total_cm//100000
        total_cm=total_cm%100000

        m=total_cm//100
        cm=total_cm%100

        if m>=1000:
            km+=m//1000
            m=m%1000
        return Distance(km,m,cm)
    
    # Overload - operator
    def __sub__(self, other):
        total_cm=(self.km*100000+self.m*100+self.cm)-\
            (other.km*100000+other.m*100+other.cm)
        km= total_cm//100000
        total_cm=total_cm%100000
        m=total_cm//100
        cm=total_cm%100
        return Distance(km,m,cm)

    # Display
    def display(self):
        print("Distance:",self.km,"km",self.m,"m",self.cm,"cm")

    #Destructor
    def __del__(self):
        print("Distance Object destroyed")

# Creating Objects
d1 = Distance(5,60,80)
d2 =Distance(2,50,70)

print("First Distance:")
d1.display()

print("Second Distance:")
d2.display()

# Addition
d3 = d1+d2
print("\nAddition:")
d3.display()

# Substraction
d4 =d1-d2
print("\nSubstraction")
d4.display()

            
        

    
