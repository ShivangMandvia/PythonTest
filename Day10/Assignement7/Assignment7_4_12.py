#12> Write a program to find sum first 100 natural numbers.

class FirstN:
    def SumofFirstN(self, num):
        x = lambda num : num*(num+1)//2
        return (x(num))



n=int(input("Enter the nth number: "))
tst = FirstN()
output = tst.SumofFirstN(n)
print(f"The sum of {n} number is {output}")