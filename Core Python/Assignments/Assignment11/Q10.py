# Write a program to print list after removing even numbers.
li = [10,15,20,25,30,35,40]

new_li = []

for i in li:
    if i % 2 != 0:
        new_li.append(i)

print("List after removing even numbers:",new_li)