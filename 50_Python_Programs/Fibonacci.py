# 0 1 1 2 3 5 8 13
n=0
m=1
n1 = int(input("Enter the number how much you wanted to print fibonacci series:\n"))
def fi(n1):
   global n, m 
   for i in range(0,n1):
            c = n + m
            n = m
            m = c
            #n, m = m, c 
            print(c)

fi(n1)