#9>	Write a program to find the sum of first n numbers.

n = int(input("Enter a Number : "))
sum = 0

for x in range(0,n+1):
    sum +=x
print("the sum of first %d numbers is : %d" %(n,sum))