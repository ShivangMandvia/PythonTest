#3>	Check a number is odd or even.

class OddEven:
    def IfEvenOrOdd(self,num):
        if (num%2==0):
            print(f"The Number {num} is Even")
        else:
            print(f"The Number {num} is Odd")

x= int(input("Enter a number :"))
a = OddEven()
a.IfEvenOrOdd(x)
