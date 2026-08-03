# Write a program to check if enterd number is palindrome or not
def palindrome (num):
    temp = num
    rev = 0

    while num > 0:
        digit = num % 10
        rev = rev * 10 + digit
        num = num//10
    if temp == rev:
        return True
    else:
        return False

n = int (input("Enter Number:"))
if palindrome (n):
    print("Palindrome Number")
else:
    print("Not a palindrome Number")