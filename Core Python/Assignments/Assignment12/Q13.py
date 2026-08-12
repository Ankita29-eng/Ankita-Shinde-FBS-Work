 # Python Program to count number of digits and letters in a string.
s = input('Enter String:')
digit = 0
letter = 0
for ch in s:
    if ch >='0' and ch <='9':
        digit = digit + 1
    elif (ch >='a'and ch <='z') or (ch>='A'and ch <='Z'):
        letter = letter + 1
print("Number of digits:",digit)
print("Number of letters:",letter)
