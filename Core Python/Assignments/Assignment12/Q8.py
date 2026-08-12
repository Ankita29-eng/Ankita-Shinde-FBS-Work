# Python Program to Remove the Characters of Odd index Values in a String.
s = input('Enter a String:')
new = ""
for i in range(len(s)):
    if i % 2 == 0:
        new = new + s[i]
print(new)