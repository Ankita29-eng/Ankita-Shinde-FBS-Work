# Python Program to count number of lowercase characters in a string
s = input('Enter String:')
count =0
for ch in s:
    if ch>='a'and ch<='z':
        count = count + 1
print("Lowecase characters:",count)