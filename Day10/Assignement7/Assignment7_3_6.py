#6>	Print First 10 numbers using for and while.

class PrintRange:
    def NumRange(self,num1,num2):
        a = list(filter(lambda x:(x+1), range(num1,num2+1)))
        print(a)
        return a

#n1 = int(input("Enter first number: "))
#n2 = int(input("Enter Last number: "))

tst = PrintRange()
#b = tst.NumRange(n1,n2)
b = tst.NumRange(1,10)

print("\nnew list :", b)

