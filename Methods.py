n1="Rishu"
n = f"my nAme is {n1}" 
print(n.capitalize()) #This method capitalize first character of a string.
print(n.casefold())
print(n.center(50))
print(n.count("n"))
print(n.endswith("u"))
print(n.endswith("hu"))

r = "E\ x\p\a\n\d\i\n\g"

print(r.expandtabs(2))
print(r.find("nAme"))
print(r.isdigit())

print(r.isdecimal())
print(n1.upper())
print(n1.swapcase()) #Convert uppercase character to lower and vice-versa.

n2 = "Welcome to australia"
print(n2.title())
print(n1.startswith("R"))
print(n1.startswith("Ri"))
print(n1.startswith("Ris"))
print(n1.startswith("Ris4"))
print(n2.islower())
sp = '   '
print(n2.isspace())
print(sp.isspace())
print(n2.encode()) #Returns the encoded version of string