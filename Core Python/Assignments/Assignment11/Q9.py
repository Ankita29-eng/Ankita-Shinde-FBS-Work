# write a program to create three lists of numbers,their squares and cubes.
li = [1,2,3,4,5]

square = list(map(lambda x:x**2,li))
cube = list(map(lambda x: x**3,li))

print("Numbers:",li)
print("Squares:",square)
print("Cubes:",cube)
