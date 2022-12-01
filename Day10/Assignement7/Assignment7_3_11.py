#11>	Write a program to find odd and even number in range of n.

class ListEvenOdd:
    def PrintEvenList(self,num):
        n = list(filter(lambda x: x%2==0,range(1,num+1)))
        return n

    def PrintOddList(self,num):
        n = list(filter(lambda x: x%2!=0,range(1,num+1)))
        return n

tst = ListEvenOdd()
n1 = int(input("Enter a number for range of even and odd number list: "))
print("The List of Even number is: ", tst.PrintEvenList(n1))
print("The List of Even number is: ", tst.PrintOddList(n1))






















#














