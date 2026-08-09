# Write a program to find sum of all elements of list
n = int (input("Enter the number of elements:"))
li = []
for i in range (n):
    num = int (input("Enter element="))
    li = li + [num]

total = 0
for i in li:
    total = total + i
print("List = ",li)
print ("Sum of all elements=",total)
