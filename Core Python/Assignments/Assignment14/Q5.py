# Write a Python program to find the longest common prefix of all strings.Use the Python set.
words = ["flower","flow","flight"]
result=""
for i in range(len(words[0])):
    s = set()

    for word in words:
        if i < len(word):
            s.add(word[i])

    if len(s) == 1:
        result = result + words[0][i]
    else:
        break
print("Longest common prefix:",result)