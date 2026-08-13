# Python Program to Concatenate Two Dictionaries Into One
dict1={'a':10,'b':20}
dict2={'c':30,'d':40}

result={}

for key in dict1:
    result[key]=dict1[key]

for key in dict2:
    result[key]=dict2[key]

print("Concatenated Dictionary:",result)
