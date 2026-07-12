# WAP to calculate selling price of book based on cost price and discount.

cp = float(input("Enter the cost price of the book:"))
discount = float(input("Enter the discount percentage:"))

discount_amount =(cp * discount)/100
sp = cp - discount_amount

print("Selling Price=", sp)