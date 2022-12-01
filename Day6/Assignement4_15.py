#5> Write a program to find the sum of digits of a number 

a=input("Enter the number : ")
sum=0
for x in range(len(a)):
    b=int(a[x])
    sum=sum+b
 
print("The sum of digits of a number is: ",sum)   
