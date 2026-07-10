# Write a program to enter P,T,R and calculate Compound Interest
P = float(input("Enter Principal (P):"))
T = float (input("Enter Time (T):"))
R = float (input("Enter Rate (R):"))

Rate = R / 100
Amount = 1 + Rate 
Power = Amount ** T
Total_Amount = P * Power
CI = Total_Amount - P

print("Compound Interest=", CI)