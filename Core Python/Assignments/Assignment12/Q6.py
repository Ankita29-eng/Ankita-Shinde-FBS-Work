# Python Program to Take in a string and Replace Every Blank Space with Hyphen
s = input('Enter string:')
new=" "
for ch in s:
    if ch == " ":
        new= new+"-"
    else:
        new=new+ch

print(new)  
