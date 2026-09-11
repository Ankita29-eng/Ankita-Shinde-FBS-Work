# Remove all of the vowels in a string(take input from user)
string = input("Enter a string:")

result =''.join([i for i in string if i not in 'aeiouAEIOU'])
print("String without vowels:",result)
