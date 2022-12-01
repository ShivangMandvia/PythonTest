#10>	Write a program to show any multiplication table.

class Multi:
    def TableForMulti(self,num):
        for i in range(1,13):
            a = lambda num:print(f"{num}x{i}={num*i}\n")
            a(num)

tst = Multi()
n =  int(input("Enter a number to print table : "))
tst.TableForMulti(n)