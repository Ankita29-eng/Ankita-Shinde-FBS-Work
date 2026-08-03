# Write a program to print Fibonacci series using recursion

# Recursive function to find fibonacci number
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci (n-1) + fibonacci(n-2)

# Input from user
n = int (input("Enter the number of terms:"))
print("Fibonacci Series :")
for i in range (n):
    print (fibonacci (i),end = " ")