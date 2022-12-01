#14> Write a program to find whether a number is prime or not. 
class Prime:
    def checkPrime(self,num):
        x = lambda n: 0 not in [n%i for i in range(2,n//2+1)]
        return x(num)

n = int(input("Enter a number to check prime or not :"))
tst = Prime()
z = tst.checkPrime(n)
if(z==True):print("It is a prime number")
else: print("It is not a Prime number")