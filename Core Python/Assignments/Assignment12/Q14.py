# Python Program to count the occurrences of each word in a string.
s = input("Enter a string:")
words= s.split()
visited = []

for word in words:
    if word not in visited:
        count = 0

        for w in words:
            if word == w:
                count = count + 1

        print(word,":",count)
        visited.append(word)