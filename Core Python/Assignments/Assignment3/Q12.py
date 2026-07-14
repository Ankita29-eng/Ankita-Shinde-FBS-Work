# Write  a program to check if given 3 digit number is a palindrome or not
num = int(input("Enter a 3-digit number:"))
if num < 100 or num > 999:
    print("Please enter a valid 3-digit number.")
else:
    temp = num
    rev = 0

    while temp > 0:
        digit = temp % 10
        rev = rev * 10 + digit
        temp = temp // 10
    if num == rev:
        print("palindrome Number")
    else:
        print("Not a Palindrome Number")