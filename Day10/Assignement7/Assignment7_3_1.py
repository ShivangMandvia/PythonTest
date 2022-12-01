#1>	Print all prime number between a range with class, function and lambda function.

class printPrime:
     def Ranger(self,FirstNumber, SecondNumber):
          if(SecondNumber>FirstNumber):
               l=list(filter(lambda x: not list(filter(lambda y : x%y==0, range(2,x))),range(FirstNumber,SecondNumber+1)))               
               return l
          else:
               print("Invalid Inputs")
               return 0
a = int(input("Enter the starting number -"))
b = int(input("Enter the Last number -"))
c = printPrime()
print(c.Ranger(a,b))

