# Write a program to check if enterd year is a leap year or not
# with parameter without Returning value
def leap_year (year):
    if (year % 400 == 0) or (year % 4== 0 and year % 100):
        print("Leap Year")
    else:
        print("Not a leap year")
year = int (input("Enter year:"))
leap_year (year)