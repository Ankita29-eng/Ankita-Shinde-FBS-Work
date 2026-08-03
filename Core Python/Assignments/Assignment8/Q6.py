# Write a program to find print the following Fibonacci series using functions:
# 1 1 2 3 5 8 n terms
# With Parameter without returning  value
def fibonacci (n):
    a=1
    b=1
    print("Fibonacci Series :")
    for i in range (n):
        print(a,end= " ")
        c=a+b
        a=b
        b=c
n =int (input("Enter number of terms:"))
fibonacci(n)
