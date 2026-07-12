# Wriite a program to swap two numbers using third variable.

x = int(input("Enter first number:"))
y = int (input("Enter second number:"))

z = x
x = y
y = z

print("After swapping:")
print ("x =", x)
print("y=",y)