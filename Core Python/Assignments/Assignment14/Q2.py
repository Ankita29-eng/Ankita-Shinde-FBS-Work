# Write a Python Program to remove the intersection of a second set with a first set.
A = {1,2,3,4,5}
B = {3,4,6,7}

common = A.intersection(B)

for x in common:
    A.remove(x)

print(A)