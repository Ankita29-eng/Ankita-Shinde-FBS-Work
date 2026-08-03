# write a program to find sum of digits of a number.
# with passing parameter with returning value
def sum_of_digits (n):
    sum = 0

    while n>0:
        digit = n % 10
        sum = sum + digit
        n = n//10
    return sum 
num = int (input("Enter a number:"))
result = sum_of_digits (num)
print("sum of digits =",result)