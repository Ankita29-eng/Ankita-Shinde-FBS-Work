# Count the numbers of spaces in a string(take input from user)
string = input ("Enter a String:")
count = sum([1 for i in string if i == ' '])
print("Number of spaces:",count)
