#4. Write a program to print the following pattern:
#     *
#    * *
#     *


a =int(input("Enter a Number :"))
n =a
i=0
for i in range(n):
    for j in range(i,n-1):
        print(" ",end=" ")     
    for j in range(i+1):
        print("*",end=" ")
        print("  ",end="")
    print("\n")
i=1
for i in range(n-1):
    for j in range(i+1):
        print(" ",end=" ")     
    for j in range(n-i-1):
        print("*",end=" ")
        print("  ",end="")
    print("\n")


