# Write a program to find factorial using recursion
def fact (n):
    if (n > 1):
        return n * fact (n-1)
    else:
        return 1
n =  int (input(" Enter a number:"))
res = fact (n)
print (res)