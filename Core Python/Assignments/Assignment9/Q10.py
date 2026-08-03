# Write a program to reverse a number using recursion
rev = 0
def reverse (n):
    global rev
    if n > 0:
        rem = n % 10
        rev = rev * 10 + rem
        reverse (n//10)
n = int (input("Enter a number:"))
reverse(n)
print("Reverse=",rev)