#19> Write a program to find the sum of all odd numbers till 100. 

class numeric:

    def SumOfAllOdd(self,n):
        SumOFDigit = sum(i for i in range(1,n+1,2))
        return SumOFDigit


num = int(input("Enter a number :"))
tst = numeric()
number = tst.SumOfAllOdd(num)
print(f"The Sum of all Odd numbers till  {num}  is {number}")
    