# Python Program to replace every blank space with hyphen in a string.
s = input("Enter String:")
for ch in s:
    if ch == ' ':
        print('-',end='')
    else:
        print(ch,end='')
