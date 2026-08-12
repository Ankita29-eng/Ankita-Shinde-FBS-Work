# Python Program to Count the number of Vowels in a string
s = input("Enter String:")
count = 0
for i in range(len(s)):
    if s[i]=='a'or s[i]=='e' or s[i]=='i' or s[i]=='o' or s[i]=='u' or s[i]=='A' or s[i]=='E' or s[i]=='I' or s[i]=='O' or s[i]=='U':
        count=count + 1
   
print(f'{count}')
