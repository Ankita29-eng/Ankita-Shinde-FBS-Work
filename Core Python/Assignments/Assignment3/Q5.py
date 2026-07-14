# Write a program to check whether the triangle is equilateral, isosceles or scalene triangle.
a = int (input ("Enter First side:"))
b = int (input("Enter Second side:"))
c = int (input("Enter third side:"))

if a == b and b == c:
    print("Triangle is Equilateral")
elif a == b or b == c or a ==c:
    print("Triangle is Isosceles")
else:
    print("Triangle is Scalene")   