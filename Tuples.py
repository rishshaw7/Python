# The main difference in list and tuple is list changeable and tuple is unchangeable.

#How to create tuple

Pens = ("Montblanc","Caran D'Ache","OMAS","Parker","Visconti","Pelikan","Aurora")

#Access elements of tuple
print(Pens[2])

#Printing all pens in the Pens tuple using for loop at once 
for pen in Pens:
    print(pen)
    
#Printing all pens in the Pens tuple using for loop in reverse order

for pen in reversed(Pens):
     print(pen)
     
#Methods in tuple
'''
1.count
2.Index
3.append
4.sort
5.reverse
etc.
'''