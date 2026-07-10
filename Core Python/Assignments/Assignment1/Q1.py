# Write a program to calculate the percentage of student based on marks of any 5 subjects
m1 = int (input("Enter marks of subject 1:"))
m2 = int(input("Enter marks of subject 2:"))
m3 = int(input("Enter marks of subject 3:"))
m4 = int (input("Enter marks of subject 4:"))
m5 = int(input("Enter marks of subject 5:"))

obtained_marks = m1 + m2 + m3 + m4 +m5
total_marks = 500

percentage =(obtained_marks/total_marks)*100

print("obtained marks=",obtained_marks)
print("percentage =", percentage,"%")      
      