# Write a program to convert days into years, weeks and days.
days = int (input('enter days:'))

years = days//365
#print(years)

days = days % 365
#print(days)

weeks = days// 7
#print(weeks)

days =days % 7
#print(days)

print(f'years:{years},Weeks:{weeks},Days:{days}.')