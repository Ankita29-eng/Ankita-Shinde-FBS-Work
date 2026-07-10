# Program to Find the Roots of a Quadratic Equation
import math
# Input
a = float (input("Enter the value of a:")) 
b = float (input("Enter the value of b:")) 
c = float (input("Enter the value of c:")) 

# Calculate the discriminant
D = b**2 - 4*a*c

# Calculate the roots
x1 = (-b + math.sqrt(D)) / (2*a)
x2 = (-b - math.sqrt(D)) / (2*a)

# Display the result
print("Root 1 =",x1)
print("Root 2 =",x2)

