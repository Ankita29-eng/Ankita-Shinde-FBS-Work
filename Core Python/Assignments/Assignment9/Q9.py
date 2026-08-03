# Write a program to calculate the m to the power n using recursion
def power(m,n):
    if n == 0:
        return 1
    return m * power (m,n-1)
m = int (input("Enter Number 1:"))
n =int (input("Enter number 2:"))
result = power (m,n)
print (f"{m} Raised to the power {n}= {result}")