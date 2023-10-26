#sets
shampoo = {"Loreal","Clinic Plus","Dove","Indulekha"}
print(shampoo)

#From list to set 
l = set([23,44,55,77])
print(shampoo)
print(len(shampoo))
print(type(shampoo))

for sh in shampoo:
    print(sh)
    
print("Dove" in shampoo) # in membership operator

print(shampoo.add("Pantene")) #add
shampoo.update(l) #Merge the set
print(shampoo)

shampoo.update(l) #Merge the set
print(shampoo)

shampoo.remove("Loreal")
print(shampoo)

#shampoo.discard("Indulekha")
#print(shampoo)

shampoo.clear()
print(shampoo)

del shampoo
print(shampoo)