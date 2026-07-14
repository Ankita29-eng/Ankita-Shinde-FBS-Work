#Input 5 subject marks from user and display grade (eg.First class,Second class ...)
m1 = float(input("Enter marks of Subject 1 :"))
m2 = float (input("Enter marks of Subject 2 :"))
m3 = float (input("Enter marks of Subject 3:"))
m4 = float (input("Enter marks of subject 4:"))
m5 = float (input("Enter marks of Subject 5:"))

total = m1 + m2 + m3 + m4 + m5 
percentage = total / 5

print("Total Marks =",total)
print("Percentage =",percentage)

if percentage >= 60:
    print("Grade: First Class")
elif percentage >= 50:
    print("Grade: Second Class")
elif percentage >= 35:
    print("Grade: Pass Class")
else:
    print("Grade: Fail")
