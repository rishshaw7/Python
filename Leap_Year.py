yr = int(input("Enter year :\n"))
if yr%4 ==0:
    print(f"{yr} is a leap year.")
if yr%4 !=0:
    print(f"{yr} is not a leap year.")
    
    #or
    
yr = int(input("Enter year:\n"))

if yr % 4 == 0:
    print(f"{yr} is a leap year.")
else:
    print(f"{yr} is not a leap year.")
    
    #or
    
y = int(input("Enter a number :"))
if y%4==0 and (y%100!=0 or y%400==0):
    print("{} is a leap year.".format(y))
else:
    print("{} is not a leap year.".format(y))
