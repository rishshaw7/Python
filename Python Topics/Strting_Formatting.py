name  = "Rishu"   #%s
print("My name is %s!"%name)  #%s
print("%s is a good boy"%name)

inr = 20
print("The cost price of pen is ₹%d."%inr)
print("The cost price of pen is ₹",20,".")

age = int(input("Enter your age :"))
message = "My name is {} and I am {} years old.".format(name,age)
print(message)

col1 = input("Enter color name :") 
col2 = input("Enter color name :")

print("My favourite color is {} and {}.".format(col1,col2))
print("My favourite color is {col2} and {col1}.".format(col1="red",col2="yellow"))
print("My favourite color is {col1} and {col2}.".format(col1="yellow",col2="red"))

print(f"My name is {name}.")

message1 = f"My name is {name} and I am {age} years old." #f{}
print(message1)
message1 = "My name is {name} and I am {age} years old.".format(name="Rishu",age=16) #str.format()
print(message1)

'''
Three ways of formatting :
1.%s
2.str.format()
3.f{}
String Formatting

%s - String (or any object with a string representation, like numbers)

%d - Integers

%f - Floating point numbers

%.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot.

%x/%X - Integers in hex representation (lowercase/uppercase)
'''