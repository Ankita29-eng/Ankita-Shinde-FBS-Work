# Python Program to Find the Union of two Lists without
# using set concept.
list1=[1,2,3,4]
list2 = [3,4,5,6]

union = list1.copy()

for i in list2:
    if i not in union:
        union.append(i)

print("Union=",union)