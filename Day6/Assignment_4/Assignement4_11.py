#11> Write a program to find factorial of a number.

a=int(input("Enter the number: "))
sum=1
if(a==0):
    print("The factorial is ",1)
else:   
    while(a>0):
        sum=sum*a
        a=a-1
    print("The factorial is ",sum)