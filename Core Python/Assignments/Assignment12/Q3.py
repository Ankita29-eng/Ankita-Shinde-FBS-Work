# Python Program to Detect if Two Strings are Anagrams
str1 = input("Enter First String:")
str2 = input("Enter second string:")

if sorted(str1)==sorted(str2):
    print("Strings are Anagram")
else:
    print("Strings are not Anagram")