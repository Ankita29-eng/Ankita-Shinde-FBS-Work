# Create a class College which has collection of students.Add the  following methods:
#a.Parameteried constructor for number of students.
#b. AddStudent
#c.GetStudent
#d.RemoveStudent
#e.Override__str__Method
class Student:
    def __init__(self,studentId,name,age,percentage):
        self.StudentId =studentId
        self.name=name
        self.age = age
        self.percentage = percentage

    def __str__(self):
        return f"ID:{self.StudentId},Name:{self.name},Age:{self.age},Percentage:{self.percentage}"

class College:
    #Parameterized constructor
    def __init__(self,numberOfStudents):
        self.students=[None]*numberOfStudents
        self.numberOfStudents = numberOfStudents

    #Add Student
    def AddStudent(self,student,index):
        if 0 <= index < self.numberOfStudents:
            self.students[index]=student
            print("Student Added Successfully")
        else:
            print("Invalid index.")

    #Get Student
    def GetStudent(self,index):
        if 0 <= index < self.numberOfStudents: return self.students[index]
        else:
            print("Invalid index.")
            return None

    # Remove Student
    def RemoveStudent(self,index):
        if 0 <= index < self.numberOfStudents:
            self.students[index]=None
            print("Student Removed Successfully")
        else:
            print("Invalid index")

    # Override __str__
    def __str__(self):
        result="College Students:\n"

        for i,student in enumerate(self.students):
            if student is not None:
                result += f"{i+1}.{student}\n"
        return result

# Create College Object
c = College(3)

# Create Student object
s1 = Student(1,"Ankita",20,85.5)
s2 = Student(2,"Vaishnai",20,90.5)
s3 = Student(3,"aaradhya",21,75.5)

#Add Students
c.AddStudent(s1,0)
c.AddStudent(s2,1)
c.AddStudent(s3,2)

#Display Students
print(c)

#Get student
print("Get Student:")
print(c.GetStudent(1))

#Remove student
c.RemoveStudent(1)

#Display After Removing
print("\n After Removing Student:")
print(c)




        


        