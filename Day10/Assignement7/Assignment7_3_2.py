#2>	Print all prime number range – n.

class printPrime:
     def RangerOnlyLastNumber(self,FirstNumber):
          if(FirstNumber>0):
               l=list(filter(lambda x: not list(filter(lambda y : x%y==0, range(2,x))),range(1,FirstNumber+1)))               
               return l
          else:
               print("Invalid Inputs")
               return 0
b = int(input("Enter the Last number -"))
c = printPrime()
print(c.RangerOnlyLastNumber(b))