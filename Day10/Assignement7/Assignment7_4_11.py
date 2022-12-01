#11> Write a program to find factorial of a number.
class FactMath:
    def Facto(self,number):
        x = lambda num : 1 if num <= 1 else num*x(num-1)        
        return x(number)
        
tst = FactMath()

number = int(input('Enter number: '))
y = tst.Facto(number)
print(f"the factorial of {number}! is {y}")