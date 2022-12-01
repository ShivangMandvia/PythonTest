#19> Write a program to find the sum of all odd numbers till 100. 

a=(list(range(1,100,2)))
sum=0
for x in range(len(a)):
    sum=sum+a[x]
print("The sum of all odd numbers till hundred is :",sum)
    