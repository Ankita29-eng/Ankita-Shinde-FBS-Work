#1.Create a class Student with following
#a. data members:
# i.StudentId
# ii.Name
# iii.Age
# iv. Percentage
#b. Add the following methods:
# i.Parameterized Constructor
# ii. Display
#iii.Accept
#iv.Method CalculateRank
#v.Override__str__Method
class Student:
    # Parameterized Constructor
    def __init__(self,StudentId,Name,Age,Percentage):
        self.StudentId =StudentId
        self.Name = Name
        self.Age = Age
        self.Percentage = Percentage

    #Accept Method
    def Accept(self):
        self.StudentId=int(input("Enter Student ID:"))
        self.Name=input("Enter Name:")
        self.Age = int(input("Enter Age"))
        self.Percentage=float(input("Enter Percentage:"))

    #Display Method
    def Display(self):
        print("Student ID:",self.StudentId)
        print("Name:",self.Name)
        print("Age:",self.Age)
        print("Percentage:",self.Percentage)
        print("Rank:",self.CalculateRank())

    # Calculate Rank method
    def CalculateRank(self):
        if self.Percentage >= 75:
            return"Distinction"
        elif self.Percentage >=60:
            return "First Class"
        elif self.Percentage >=50:
            return"Second Class"
        elif self.Percentage >=35:
            return "pass"
        else:
            return "Fail"

    # Override __str__method
    def __str__(self):
        return f"StudentId:{self.StudentId},Name:{self.Name},Age:{self.Age},Percentage:{self.Percentage}"

# Object creation using parameterized constructor
s1 = Student(101,"Ankita",21,85.50)

#Display
s1.Display()

#__str__method
print("\nStudent Object:")
print(s1)