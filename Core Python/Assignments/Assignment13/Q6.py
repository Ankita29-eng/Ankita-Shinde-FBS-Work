# Python Program to Multiply All the Items in a Dictionary
d = {'a':10,'b':3,'c':2}
multiply = 1
for value in d.values():
    multiply = multiply*value
print(f' Multiplication all the items in a dictionary:{multiply}')
