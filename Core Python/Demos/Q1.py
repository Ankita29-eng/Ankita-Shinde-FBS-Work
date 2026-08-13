path = "WNEENES" 
x = 0
y = 0

for  i in path:
    if i=="N":
        y+=1

    elif i == "S":
        y-=1

    elif i == "W":
        x-=1

    elif i == "E":
        x+=1
    else:
        print("Invalid Path")
        break
print("Final Cordinate",(x,y))  
dist=((x**2)+(y**2))**0.5
print(f"Total distance traveled by the Person={dist}")