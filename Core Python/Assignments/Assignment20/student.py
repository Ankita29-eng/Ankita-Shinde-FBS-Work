from SY.symarks import SYMARKS
from TY.tymarks import TYMARKS

class Student:
    def __init__(self,roll_no,name):
        self.roll_no= roll_no
        self.name = name

        self.sy = None
        self.ty = None

    def accept (self):
        computer=int(input("Enter SY Computer marks:"))
        maths = int(input("Enter SY Maths marks:"))
        electronics = int(input("Enter SY Electronics marks:"))
        theory=int(input("Enter TY Theory Marks:"))
        practical = int(input("Enter TY Practical Marks:"))


        self.sy = SYMARKS(computer,maths,electronics)
        self.ty = TYMARKS(theory,practical)

    def calculate(self):
        total = (
            self.sy.computer+
            self.sy.maths+
            self.sy.electronics+
            self.ty.theory+
            self.ty.practical
                                
        )

        percentage = total / 5

        if percentage >= 70:
            grade ="A"
        elif percentage >=60:
            grade="B"
        elif percentage >=50:
            grade ="C"
        elif percentage >=40:
            grade ="Pass Class"
        else:
            grade="Fail"

        return total,percentage,grade
    def display(self):
        total,percentage,grade=self.calculate()

        print("\n-------STUDENT RESULT------")
        print("Roll Number:",self.roll_no)
        print("Name:",self.name)
        print("SY Computer:",self.sy.computer)
        print("SY Maths:",self.sy.maths)
        print("SY Electronics:",self.sy.electronics)
        print("TY Theory:",self.ty.theory)
        print("TY Practical:",self.ty.practical)
        print("Total Marks:",total)
        print("Percentage:",percentage)
        print("Grade:",grade)
s = Student(101,"Ankita")
s.accept()
s.display()

        