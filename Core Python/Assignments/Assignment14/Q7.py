# Given two sets of numbers, 
# write a Python program to find the missing numbers in the second set as compared to the first 
# and vice versa. Use the Python set.
A = {1,2,3,4,5}
B = {3,4,5,6,7}

print("Missing in B:")

for x in A:
    if x not in B:
        print(x)

print("Missing in A:")

for x in B:
    if x not in A:
        print(x)