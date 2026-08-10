# Python Program to Sort the list According to the Second Element in Sublist.
li = [[1,5],[2,3],[3,8],[4,1]]
li.sort(key = lambda x:x[1])
print("Sorted List:",li)