side1 = float(input("Enter First  side of  a triangle"))
side2 = float(input("Enter Second side of a triangle :"))
side3 = float(input("Enter Third  side of a triangle :"))

if side1==side2==side3:
    print("The triangle is a Equilateral.")
if side1==side2 or side2==side3 or side3==side1:
    print("The triangle is a Isosceles.")
else:
    print("The triangle is Scalene.")
    
#or

side1 = float(input("Enter the first side of a triangle: "))
side2 = float(input("Enter the second side of a triangle: "))
side3 = float(input("Enter the third side of a triangle: "))

if side1 == side2 == side3:
    print("The triangle is an Equilateral.")
if side1 == side2 or side2 == side3 or side3 == side1:
    print("The triangle is an Isosceles.")
if side1 != side2 and side2 != side3 and side3 != side1:
    print("The triangle is a Scalene.") 
