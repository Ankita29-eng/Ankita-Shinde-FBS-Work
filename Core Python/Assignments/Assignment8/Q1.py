# Write a program to calculate area of rectangle
# with parameter with returning value
def rectangle_area (length,width):
    area = length*width
    return area
 # Input from user
length = float(input("Enter length:"))
width = float(input("Enter width :"))

#Function Call
result = rectangle_area(length,width)

# Display result
print("Area of rectangle =",result)
