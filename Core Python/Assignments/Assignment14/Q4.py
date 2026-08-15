# Write a Python Program that finds all pairs of element in a list 
# whose sum is equal to a given value.
li = [2,4,3,5,7]
value = 7

for i in range(len(li)):
    for j in range(i+1,len(li)):
        if li[i]+li[j] == value:
            print(li[i],li[j])