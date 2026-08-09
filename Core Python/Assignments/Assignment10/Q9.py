# Write a program of having n number of elements in the list and 
# find out even and odd elements in that list and then create two separate lists which will have even elements
# and other will have odd elements.

n = int (input("Enter number of elements:"))
li = []
for i in range(n):
    num = int(input("Enter element:"))
    li += [num]

even = []
odd = []

for i in li:
    if i % 2 == 0:
        even += [i]
    else:
        odd += [i]

print("Original List:",li)
print("Even List:",even)
print("Odd List:",odd)