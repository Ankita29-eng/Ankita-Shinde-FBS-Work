n= int (input("Enter Input:"))
coins = list(map(int,input().split()))
missing = 0
for coin in coins:
    missing = missing ^ coin
print(missing)