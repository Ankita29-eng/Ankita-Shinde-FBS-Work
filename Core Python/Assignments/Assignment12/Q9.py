# Python Program to Calculate the Number of Words and the Number of Characters Present in a string
s = "I am good"
word = 1
char = 0

for ch in s:
    if ch == ' ':
        word = word + 1
    else:
        char = char + 1
print("Number of words:",word)
print("Number of characters:",char)
