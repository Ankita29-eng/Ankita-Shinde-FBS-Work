# Python Program to Find the Second Largest Number in a List Using Bubble Sort.
li = [10,50,30,40,20]

# Bubble Sort
for i in range(len(li)):
    for j in range(0,len(li)-i-1):
        if li[j]>li[j+1]:
            li[j],li[j+1]=li[j+1],li[j]

print("Sorted List:",li)
print("Second Largest Number:",li[-2])