# Write a program to solve the following series:
# a.1! + 2! + 3! + 4! + ...n!
#b.N + N^2 + N^3 + N^4 ...N^N (here ^ means exponent)
#c.Find the sum of a geometric series from 1 to n where the common ratio is 2.
#d. S=a+a2/2+a3/3+ .... +a10/10
#e. x-x2/3 + x3/5 - x4/7 + ...to n terms

# a.1! + 2! + 3! + 4! + ...n!
n = int (input("Enter n:"))

fact = 1
sum = 0

for i in range(1, n+1):
    fact *= i
    sum += fact
print ("Sum =",sum)

#b.N + N^2 + N^3 + N^4 ...N^N (here ^ means exponent)
n = int (input("Enter N:"))

sum = 0

for i in range (1, n + 1):
    sum += n ** i

print("Sum=",sum)

#c.Find the sum of a geometric series from 1 to n where the common ratio is 2.
n = int (input ("Enter number of terms:"))

sum = 0
term = 1

for i in range (n):
    sum += term
    term *= 2
print("Sum=",sum)

#d. S=a+a2/2+a3/3+ .... +a10/10

a = int (input("Enter value of a:"))
sum = 0
for i in range (1,11):
    sum += (a ** i)/ i
print("Sum=",sum)

#e. x-x2/3 + x3/5 - x4/7 + ...to n terms

x = int (input("Enter value of x:"))
n = int (input("Enter number of terms:"))

sum = 0
sign = 1
denominator = 1

for i in range (1, n + 1):
    sum += sign *(x ** i)/ denominator
    sign *= -1
    denominator += 2

print("Sum =", sum)



