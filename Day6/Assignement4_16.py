#16> Write a program to find the first n numbers in a Fibonacci series


n=int(input("Enter the value of n: "))
print("Thus the fibo series till ",n,"th term is: ")
t1=0
t2=1
tn=t1+t2
if(n==1):
    print(0)
elif(n==2):
    print(0)
    print(1)
elif(n>2):
    print(t1)
    print(t2)
    for x in range(n-2):
        print(t1+t2)
        tn=t1+t2
        t1=t2
        t2=tn