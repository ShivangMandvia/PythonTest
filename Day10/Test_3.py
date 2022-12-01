#write a program check a number is odd or even , prime or not

class OddEven:
    def IfEvenOrOdd(self,num):
        if (num%2==0):
            print("The Number is Even")
        else:
            print("The Number is Odd")


    def is_prime(self,n):
        for i in range(2,n):
            if (n%i) == 0:
                print("The Number is Not Prime")
                exit()
        print("The Number is Prime")

x= int(input("Enter a number :"))
a = OddEven()

a.IfEvenOrOdd(x)
a.is_prime(x)