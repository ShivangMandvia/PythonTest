#3> Write a program to find the sum of all Odd and Even numbers up to a number specified by the user

class ListEvenOdd:
    def SumofEvenList(self,num):
        n = list(filter(lambda x: x%2==0,range(1,num+1)))
        Total = sum(n)
        return Total

    def SumofOddList(self,num):
        n = list(filter(lambda x: x%2!=0,range(1,num+1)))
        Total = sum(n)
        return Total

tst = ListEvenOdd()
n1 = int(input("Enter a number for range of even and odd number list: "))
print("The List of Even number is: ", tst.SumofEvenList(n1))
print("The List of Even number is: ", tst.SumofOddList(n1)) 