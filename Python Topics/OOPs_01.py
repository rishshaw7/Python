#How to create a class
class company:

    def __init__(self,firm_n,Estd):
         self.firm_n = firm_n
         self.Estd = Estd
        
obj2 = company("REHR",1997)
print(obj2.firm_n)
print(obj2.Estd)