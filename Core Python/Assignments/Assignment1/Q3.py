# Program to find quotient and remainder of two numbers.

dividend = int(input("Enter Dividend:"))
divisor = int(input("Enter Divisor:"))

quotient = dividend // divisor
remainder = dividend % divisor

print("Quotient =", quotient)
print("Remainder =", remainder)