# Write a program to find sum of following series using Recursive Functions:
# i. 1! + 2! +3! + 4!+..........+n!
# for fact and sum two recursive functions

# Recursive function to find factorial
def fact (n):
    if n == 0 or n == 1:
        return 1
    return n * fact (n-1)

# Recursive function to find sum of series
def sum_series (n):
    if n == 1:
        return fact (1)
    return fact(n)+ sum_series(n-1)

#Main Program
n =int (input("Enter the value of n:"))
result = sum_series(n)

print("Sum of Series=",result)
