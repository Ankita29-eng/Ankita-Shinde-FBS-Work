area = float(input("Enter area of one wall="))
interior_cost = float(input("Enter interior paintaining cost="))
exterior_cost = float (input("Enter exterior paintaining cost="))

interior_area = 2*area
exterior_area = 6*area

interior_paintaining_cost = interior_area * interior_cost
exterior_paintaining_cost = exterior_area * exterior_cost

total_cost = interior_paintaining_cost + exterior_paintaining_cost
print("Interior_paintaining_cost =",interior_paintaining_cost)
print("exterior_paintaining_cost=",exterior_paintaining_cost)
print("Total Paintaining Cost=",total_cost)