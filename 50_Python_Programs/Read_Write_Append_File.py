m = open('Programs.txt','r')
print(m.read())
m.close()

n = open('p1.txt','w')
n.write('Hello, This is a 17 year old programmer.')
n.close()

o = open('p2.txt','r')
print(o.read())
o.close()