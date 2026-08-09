# Write a program to remove all occurrences of given element in the list.
li = [10,20,10,30,10,40,50]
num = int(input("Enter element to remove:"))
new_li = []
for i in li:
    if i!= num:
        new_li += [i]
print("Original List:",li)
print("New List:",new_li)