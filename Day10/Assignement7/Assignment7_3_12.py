#12>Write a program to find odd and even number between any range

class ListEvenOdd:
    def PrintEvenList(self,num1,num2):
        n = list(filter(lambda x: x%2==0,range(num1,num2+1)))
        return n

    def PrintOddList(self,num1, num2):
        n = list(filter(lambda x: x%2!=0,range(num1,num2+1)))
        return n

tst = ListEvenOdd()
n1 = int(input("Enter a 1st number for range of even and odd number list: "))
n2 = int(input("Enter a 2nd number for range of even and odd number list: "))
print("The List of Even number is: ", tst.PrintEvenList(n1,n2))
print("The List of Even number is: ", tst.PrintOddList(n1,n2))




