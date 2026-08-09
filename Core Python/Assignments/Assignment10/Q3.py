# Write a program to find the second largest element in the list.
numbers = [10,25,8,45,30]

largest = numbers[0]
second_largest = numbers[0]

for num in numbers:
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest and num != largest:
        second_largest = num

print("Second Largest Element =",second_largest)