#3. Write a program that accepts user input and prints a star pattern in pyramid format.

a =int(input("Enter a Number :"))
n =a
i=0
for i in range(n):
    for j in range(i,n-1):
        print("_",end=" ")     
    for j in range(i):
        print("*",end=" ")
    for j in range(i+1):
        print("*",end=" ")
    print("\n")

