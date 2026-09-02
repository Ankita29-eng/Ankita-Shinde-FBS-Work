#Create a derived class from Student as EnggStudent with:
# a.Data members as:
# i.Branch
#ii.InternalMarks
# b.Add the following methods:
#1.Parameterized Constructor
#2.Display
#3.Accept
#4.override Method CalculateRank
#5.Override__str__Method
class Student:
    def __init__(self,studentId =0,name="",age=0,percentage=0):
        self.StudentId= studentId
        self.name = name
        self.age = age
        self.percentage = percentage
    def display(self):
        print("Student Id:",self.StudentId)
        print("Name:",self.name)
        print("Age:",self.age)
        print("percentage:",self.percentage)
    def Accept(self):
        self.StudentId=int(input("Enter Student Id:"))
        self.name=input("Enter Name:")
        self.age = int(input("Enter Age:"))
        self.percentage=float(input("Enter Percentage:"))
    def CalculateRank(self):
        if self.percentage>=75:
            return "Distinction"
        elif self.percentage>=60:
            return "First Class"
        elif self.percentage>=50:
            return "Second Class"
        elif self.percentage>=35:
            return "pass"
        else:
            return "Fail"

    def __str__(self):
        return f"Student ID:{self.StudentId},Name:{self.name},Age:{self.age},Percentage:{self.percentage}"

# Derived Class
class EnggStudent(Student):

    #Parameterized Constructor
    def __init__(self, studentId=0, name="", age=0, percentage=0, branch="" ,internalMarks=0):
        super().__init__(studentId, name, age, percentage)
        self.branch = branch
        self.internalMarks =internalMarks

    # Override Display
    def display(self):
        super().display()
        print("Branch:",self.branch)
        print("Internal Marks:",self.internalMarks)
        print("Rank:",self.CalculateRank())

    # Override Accept
    def Accept(self):
        super().Accept()
        self.branch =input("Enter branch:")
        self.internalMarks = float(input("Enter Internal Marks:"))

    # Override CalculateRank
    def CalculateRank(self):
        total = self.percentage + self.internalMarks

        if total>=150:
            return"Excellent Rank"
        elif total>=120:
            return"Good Rank"
        elif total>=90:
            return"Average Rank"
        else:
            return "Needs Improvement"

    #Override str
    def __str__(self):
        return (f"Student ID:{self.StudentId},Name:{self.name},"f"Age:{self.age},Percentage:{self.percentage},"f"Branch:{self.branch},Internal Marks:{self.internalMarks}")

#Object Creation
e1= EnggStudent(101,"Ankita",21,80,"Computer",70)

#Display
e1.display()

#__str__Method
print("\nUsing __str__:")
print(e1)

#Calculate Rank
print("\nRank:",e1.CalculateRank())

    