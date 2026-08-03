# Write a program to check whether a number is prime or not using recursion
def is_prime (num , i):
    if num <= 1:
        return False
    if i == 1:
        return True
    if num % i == 0:
        return False
    return is_prime (num,i-1)
num= int (input("Enter a number:"))
if is_prime (num,num // 2):
    print("Prime Number")
else:
    print("Not a Prime Number")