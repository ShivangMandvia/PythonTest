#1. Write a program to check whether a number’s reverse form is its palindrome or not.

n = int(input("Enter a number :"))

a = n
Rsum=0
while(n>0):
    temp=n%10
    Rsum=Rsum*10+temp
    n=n//10
if(a==Rsum):
    print(a, "is a palindrome")
else: 
    print(a, "is not a palindrome")
