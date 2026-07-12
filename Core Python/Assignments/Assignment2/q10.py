# Write a program to reverse three digit number.
n = int (input("Enter a three-digit number:"))

r1 = n % 10
n = n // 10

r2 = n % 10
n = n // 10

r3 = n

reverse = (r1 * 100) + (r2 * 10) + r3

print("Reverse number=", reverse)