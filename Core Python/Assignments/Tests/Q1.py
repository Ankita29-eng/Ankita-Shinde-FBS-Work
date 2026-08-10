#1. Write a program to find the area and perimeter of following figure (Accept the
#length, breadth and radius from user:
import math

length = float(input("Enter length: "))
breadth = float(input("Enter breadth: "))
radius = float(input("Enter radius: "))

# Area of rectangle
area_rectangle = length * breadth

# Area of semicircle
area_semicircle = (math.pi * radius * radius) / 2

# Total area
area = area_rectangle + area_semicircle

# Perimeter
perimeter = (2 * length) + breadth + (math.pi * radius)

print("Area =", area)
print("Perimeter =", perimeter)