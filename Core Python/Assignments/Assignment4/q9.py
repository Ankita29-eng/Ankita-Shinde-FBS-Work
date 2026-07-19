# WAP to print all numbers in a range divisible by a given number.
start = int (input("Enter starting number:"))
end = int (input("Enter ending number:"))
d = int(input("Enter divisor:"))

print("Numbers divisible by",d,"are:")

for i in range(start, end + 1):
    if i % d == 0:
        print(i)