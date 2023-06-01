a = int(input("Enter a first number :"))
b = int(input("Enter a second number :"))
c = int(input("Enter a third number :"))
if a > b and a > c:
    print("{} is the greatest number.".format(a))
if b > a and b > c:
    print("{} is the greatest number.".format(b))
if c > b and c > a:
    print("{} is the greatest number.".format(c))
    
    #or
    
a, b, c = map(int, input().split())

largest = max(a, b, c)

print(f"{largest} is the greatest number.")