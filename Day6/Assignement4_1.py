#1> Write a program to display the Fibonacci sequences up to nth term where n is provided by the user.

a =0
b=1
c = 1
n = int(input("Ener a number"))
print(0,"\n")
for x in range(0,n+1):
    print(c,"\n")
    c=a+b
    a=b
    b=c
