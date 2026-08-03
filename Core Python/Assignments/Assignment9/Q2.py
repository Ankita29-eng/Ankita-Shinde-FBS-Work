# Write a program to check if given number is Armstrong or not using recursive function
def checkArmstrong (num):
    count = len (str(num))
    sum = 0
    while num > 0:
        digit = num % 10
        sum = sum + digit ** count
        num = num // 10
    return sum
num = int (input("Enter the number : "))
result = checkArmstrong (num)

if result == num :
    print(f"{num} is Armstrong Number")
else:
    print (f"{num} is not Armstrong Number")