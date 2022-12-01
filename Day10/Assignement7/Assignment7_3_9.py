#9>	Write a program to find the sum of first n numbers.

class numeric:

    def FirstNSum(self,n):
        SumOFDigit = lambda n:n*(n+1)//2
        return SumOFDigit(n)


num = int(input("Enter a number :"))
tst = numeric()
number = tst.FirstNSum(num)
print(f"The Sum of first {num} number is {number}")