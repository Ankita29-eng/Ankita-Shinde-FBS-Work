# Python Program to Remove the Given Key from a Dictionary
d = {1:10,2:20,3:30}
key = int(input('Enter Key to remove:'))
del d[key]
print("Dictionary after removing key:",d)
