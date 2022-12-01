#3> Write a program to find the sum of all Odd and Even numbers up to a number specified by the user

evenNo=0
oddNo=0
sum=0
n=int(input("Enter the value of n for the range:"))

for x in range(0,n+1,2):
    sum=sum+x
print("The Sum of even numbers from 0 to",n," is:",sum) 
#print("The Sum of  odd numbers is: ",sum)  
sum = 0
for x in range(1,n+1,2):
    sum=sum+x
print("The Sum of odd  numbers from 0 to",n," is:",sum) 
#print("The Sum of  odd numbers is: ",sum)