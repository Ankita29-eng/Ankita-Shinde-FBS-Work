# Sum of all prime numbers between 1 to n
# Without Passing parameter Without Returning value
def prime_sum ():
    n = int (input("Enter n :"))
    total = 0

    for i in range(2,n+1):
        count = 0
        for j in range (1,i+1):
            if i%j == 0:
                count += 1

        if count == 2:
            total += i

    print("sum of prime numbers=", total)
prime_sum ()