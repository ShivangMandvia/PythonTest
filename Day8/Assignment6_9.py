#9>	Write a program to find the sum of first n numbers, using function and lambda function

def FirstNSum(n):
    sum = 0
    for x in range(0,n+1):
        sum +=x
    return sum

num = int(input("Enter a Number : "))
total = FirstNSum(num)
print("the sum of first %d numbers is : %d" %(num,total))
