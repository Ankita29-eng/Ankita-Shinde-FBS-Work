# Write a program to find sum of the following series using functions:
#a. 1 + 2 + 3 +  4+......+n
#b. 1! + 2! + 3! + 4!+.....+n!
#c. 1^1 + 2^2 + 3^3 +........n^n

#a. 1 + 2 + 3 +  4+......+n
def sum_series(n):
    s = 0
    for i in range(1,n+1):
        s = s + i
    return s
n = int (input("Enter n:"))
print("Sum=",+sum_series(n))


#b. 1! + 2! + 3! + 4!+.....+n!
def factorial(num):
    fact = 1
    for  i in range (1,num+1):
        fact = fact * i
    return fact
def sum_factorial(n):
    s = 0
    for i in range(1,n+1):
        s = s+ factorial(i)
    return s
n = int (input('Enter number:'))
print("sum =",sum_factorial(n))


#c. 1^1 + 2^2 + 3^3 +........n^n
def power_sum(n):
    s=0
    for i in range(1,n+1):
        s = s+(i**i)
    return s
n = int(input("Enter number:"))
print("sum =",power_sum(n))


    

