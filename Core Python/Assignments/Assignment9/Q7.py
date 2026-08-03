# Write a program to find sum of digits using recursion
def sum_digits (n):
    if n == 0:
        return 0
    return (n%10) + sum_digits(n//10)
num = int (input("Enter a three digit number:"))

if 100<= num <=999:
    print("Sum of digits=",sum_digits(num))
else:
    print ("Please enter a valid three digit number.")