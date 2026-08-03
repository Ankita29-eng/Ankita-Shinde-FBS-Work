# WAP to check if a given number is Armstrong number or not. For each task create separate functions

def count_digits (num):
    count = 0
    temp = num
    while temp > 0:
        count += 1
        temp = temp // 10
    return count

def armstrong_sum(num,digits):
    total = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        total += digit ** digits
        temp = temp // 10
    return total

def check_armstrong (num):
    digits = count_digits (num)
    total = armstrong_sum (num , digits)

    if total == num:
        return True
    else:
        return False

n = int (input ("Enter a number : "))

if check_armstrong (n):
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")