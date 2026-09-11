# Find all of the words in a string that are less than 5 letters
# (take input from user)
string = input("Enter a String:")

result = [word for word in 
string.split() if len(word)<5]

print("Words having less than 5 letters:",result)