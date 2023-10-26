#In python string can be assigned using single quote

bro = 'Shri Madhava'
print(bro)
print("Double Quotes")
print('Single Quotes')

#String Methods

print(len(bro))
print(bro.index('a'))
print(bro.count('a'))
print(bro.split())
print(bro.upper())
print(bro.lower())
print(bro.startswith('S'))
print(bro.startswith('Shri'))
print(bro.endswith('a'))
print(bro.endswith('Madhava'))

#String Slicing

a = 'Replica, the solo learner.'
print(a[:3])
print(a[-1])
print(a[:-1])
print(a[len(a):-1])
print(a[:len(a)])
print(a[0:len(a):2]) #Skipping 1 characters from the string
print(len(a))
print(a[0:26:3]) #Skipping 2 characters from the string
print(a[0:25])
print(a[0:26])
print(a[::-1]) #Reversing the string
print(a[-26:-1])



