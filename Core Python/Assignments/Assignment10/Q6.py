# Write a program to remove duplicates from the list
li = [10,20,10,30,20,40,30]
new_li = []

for i in li:
    found = 0

    for j in new_li:
        if i == j:
            found = 1
            break

    if found == 0:
            new_li += [i]

print("Original List =",li)
print("List after removing duplicates=",new_li)