# Write a program find reverse of a number
# Without Parameter with returning value
def reverse_number():
    num =int (input("Enter a number:"))
    rev = 0
    while num>0:
        digit = num % 10
        rev = rev *10 + digit
        num = num // 10
    return rev
ans = reverse_number ()
print (" Reverse Number=",ans)