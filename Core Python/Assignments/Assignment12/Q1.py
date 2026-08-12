# Python Program to Replace all Occurrences of 'a' with $ in a string
s = input ("Enter a string")
new = " "

for ch in s:
    if ch == 'a':
        new = new + '$'
    else:
        new = new + ch

print(new)