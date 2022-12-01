#5. Write a program to multiply the digits of a number

n = int(input("Enter a number: "))
multi =1
temp = n
while(temp!=0):
    dig=temp%10
    multi = multi * dig
    temp = temp//10

print("Multiplication of ",n, "is ",multi)

