# Write a Python program to find the two numbers 
# whose product is maximum among all the pairs in a given list of numbers.
# Use the Python set.
s = {2,5,3,4}
max_product = 0

for x in s:
    for y in s:
        if x != y:
            product = x*y
            if product > max_product:
                max_product = product
                num1=x
                num2=y

print("Two numbers:",num1,num2)
print("Maximum product:",max_product)