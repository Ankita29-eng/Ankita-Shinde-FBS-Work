# Write a program to accept an integer amount from user and tell minimum number of notes needed for representing that amount.

amt = int (input("Enter amount:"))

n2000 = amt // 2000
amt = amt % 2000

n500 = amt // 500
amt = amt % 500

n200 = amt // 200
amt = amt % 200

n100 = amt //100
amt = amt % 100

print("2000 Notes =",n2000)
print("500 Notes =",n500)
print("200 Notes =",n200)
print("100 Notes =",n100 )
print("Remaining Amount =", amt)
