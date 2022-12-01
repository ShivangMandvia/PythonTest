#20> Write a program – multiplication table any two numbers. 

class Multi:
    def TableForMulti(self,num):
        for i in range(1,13):
            a = lambda num:print(f"{num}x{i}={num*i}\n")
            a(num)

tst = Multi()
n1 =  (int(input("Enter the number1: ")))
n2 =  (int(input("Enter the number2: ")))
tst.TableForMulti(n1)
tst.TableForMulti(n2)

