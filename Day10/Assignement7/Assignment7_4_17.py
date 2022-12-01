#17> Write a program to find the factorial of number n. 

class FactMath:
    def Facto(self,number):
        x = lambda num : 1 if num <= 1 else num*x(num-1)        
        return x(number)
        
tst = FactMath()

number = int(input('Enter number: '))
y = tst.Facto(number)
print(f"the factorial of {number}! is {y}")