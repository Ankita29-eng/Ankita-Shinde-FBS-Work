# Write a program to check if given number is Armstrong number or not.
#(Hint: 153 = 1*1*1 + 5*5*5 + 3*3*3 , 1634 = 1*1*1*1 + 6*6*6*6 + 3*3*3*3 + 4*4*4*4)
no = int (input("Enter the number you want to check="))
count = len(str(no))
temp = no
total = 0
while no>0:
    d = no%10
    total = total+(d**count)
    no = no//10
    print(total)
if total == temp:
    print("The number is ArmStrong")
else:
    print("The number is not Armstrong")