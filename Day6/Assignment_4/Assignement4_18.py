#18> Write a program to find the sum of any five integers. 

a=input("Enter the five numbers: ").split(" ")
sum=0
for x in range(len(a)):
    b=int(a[x])
    sum=sum+b
print("The sum of the five nums is:", sum)   

