n = int(input("Enter a number to be check wether it is a prime number or not.\n"))
k=0
for i in range(2,n): #2 10(n)-1
    if n%i==0:
        print(n," is not a prime number.")
        break
    else:
        k=1

if k==1:
    print(n," is a prime number.")