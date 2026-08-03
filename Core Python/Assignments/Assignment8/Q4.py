# Sum of all odd numbers between 1 to n
def odd_sum (n):
    s = 0
    for i in range (1,n+1,2):
        s = s+i
    return s
n = int (input("Enter Number: "))
ans = odd_sum(n)
print("sum = ",ans)

    