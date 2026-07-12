# Convert distant given in feet and inches into meter and centimeter.

feet = float(input("Enter distance in feet:"))
inches = float (input("Enter distance in inches:"))

total_inches = (feet*12) + inches
centimeter = total_inches * 2.54
meter = centimeter/100

print("Distance in Meter=",meter)
print("Distance in Centimeter=",centimeter)