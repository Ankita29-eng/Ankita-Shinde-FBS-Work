# write a program to create three lists of numbers, their squares and cubes.
li = [1,2,3,4,5]

num = []
square = []
cube = []

for i in li:
    num += [i]
    square += [i * i]
    cube += [i * i * i]

print("Numbers:",num)
print("Squares:",square)
print("Cubes:",cube)