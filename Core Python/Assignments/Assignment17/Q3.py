# Create a class MedicalStudent inherited from student with following
#i.Data Members:Specialization
#ii.MarksOfIntership

#b.Add the following methods:
#i.Parameterized Constructor
#ii.Display
#iii.Accept
#iv.override Method Calculate Rank
#v.Override__str__Method
class Student:
    def __init__(self,studentId,name,age,percentage):
        self.StudentId = studentId
        self.name = name
        self.age =age
        self.percentage =percentage

    def display(self):
        print("Student ID:",self.StudentId)
        print("Name:",self.name)
        print("Age:",self.age)
        print("Percentage:",self.percentage)

    def Accept(self):
        
        self.StudentId=int(input("Enter Student Id:"))
        self.name=input("Enter Name:")
        self.age=int(input("Enter Age:"))
        self.percentage=float(input("Enter Percentage:"))

    def CalculateRank(self):
        if self.percentage >=75:
            return"Distinction"
        elif self.percentage >=60:
            return"First Class"
        elif self.percentage >=50:
            return"pass"

    def __str__(self):
        return f"{self.StudentId}{self.name}{self.age}{self.percentage}"

class MedicalStudent(Student):
    def __init__(self, studentId, name, age, percentage,specialization,MarksOfIntership):
        super().__init__(studentId, name, age, percentage)
        self.specialization=specialization
        self.MarksOfIntership =MarksOfIntership

    def display(self):
        super().display()
        print("Specialization=",self.specialization)
        print("Marks of Intership:",self.MarksOfIntership)

    def Accept(self):
         super().Accept()
         self.specialization=input("Enter Specialization:")
         self.MarksOfIntership=float(input("Enter Marks of Intership:"))
         
    # Overriding CalculateRank
    def CalculateRank(self):
        total=self.percentage+self.MarksOfIntership
        if total >=160:
            return"Distinction"
        elif total>=130:
            return"First Class"
        elif total>=100:
            return"Second Class"
        else:
            return "pass"

    #Overriding__str__
    def __str__(self):
        return (f"StudentId:{self.StudentId},Name:{self.name},"f"Age:{self.age},Percentage:{self.percentage},"f"Specialization:{self.specialization},"f"Intership Marks:{self.MarksOfIntership}")

#Object Creation
m1 = MedicalStudent(32,"Vaishnavi",20,90.5,"Cardiology",85)
m1.display()
print("Rank:",m1.CalculateRank())
print("\nString Representation:")
print(m1)
    

        