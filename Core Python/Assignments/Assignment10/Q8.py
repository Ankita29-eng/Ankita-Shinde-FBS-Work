# Write a program to create a duplicate of an existing list .It should not point to same list.

li = [10,20,30,40,50]
new_li = []
for i in li:
    new_li += [i]

print("Original List:",li)
print("Duplicate List:",new_li)