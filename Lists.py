#List of an integer type

numbers = [32,54,77,43,22]
print(numbers) #It prints all elements in list
print(numbers[2]) #It Print specific element
print(numbers[0:3]) #It Print elements in range


#List of a String type

names = ["rishu","anshu","piyush","aman"]
print(names) 
names.append("Navin ul Haque")  # Adding element to list
print(names)

print(names[0]) 

#Creating an empty list

emp = []
print(emp)


#List with multiple type values

mixed = [133,534,"Surya",3444,"Vijay",57.4]
print(mixed)

#Multidimensional Lists harpot=Harry Potter

harpot = [1997,[1998,1999,2000,2003],2005,2007]
print(harpot[1][3])

print(harpot[-1]) #Accessing  list element using negative indexing

print(len(harpot))

#String to List

Fruits = input("Enter 5 fruit names :")
Fruits = Fruits.split()
print(Fruits)
print(type(Fruits))

#Methods in list

#1.Append
List = []
List.append(22) #Adding elements in list list type
List.append(34)
List.append(44)
List.append(55)

print(List)     

for i in range(55,61):
    List.append(i)
    
print(List)

#2.Reverse
#Number variable list is created at the top of  the code
numbers.reverse()
print(numbers)

#3.Remove
num1 = [12,13,14,15,16]
num1.remove(12)
print(num1)
print(*num1) # It removes Brackets and commas from the list 
