# Python Program to Find the Union of two Lists.
li1 = [10,20,30,40]
li2 = [30,40,50,60]

union = list(set(li1).union(set(li2)))

print("First list=",li1)
print("Second list=",li2)
print("Union of two lists=",union)