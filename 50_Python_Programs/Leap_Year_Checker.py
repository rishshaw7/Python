y = int(input("Enter a Year:\n"))

if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):
    print(y, "is a leap year.")
else:
    print(y, "is not a leap year.")







#If year is divisible by 400 or 4 that year is called leap year
#If year is divisible by 100 that year is not called as leap year if it also divisble by 400 or 4.