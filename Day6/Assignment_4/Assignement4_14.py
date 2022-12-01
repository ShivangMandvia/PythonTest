#14> Write a program to find whether a number is prime or not. 

a=int(input("Enter the number: "))
count=0

for x in range(2,a):
    if(a%x==0):
        count=count+1
        break
if(count!=0)or(a<2):
    print("The number is not prime.")
elif(count==0)or(a==2):
    print("The number is prime.")