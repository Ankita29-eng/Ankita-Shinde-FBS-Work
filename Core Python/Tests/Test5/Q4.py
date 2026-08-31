data = [1,3,4,1,2,3,6,7,1,2,4]
freq = {}

for i in data:
    if i in freq:
        freq[i] = freq[i]+1
    else:
        freq[i]=1
print(freq)