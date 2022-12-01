#11>	Write a program to find odd and even number in range of n.

n =  int(input("Enter a Number : "))
ListEven =[]
ListOdd = []

for i in range(1, n+1):
    if i%2 == 0:
        ListEven.append(i)
    else:
        ListOdd.append(i)

print("These are the Even number's :",ListEven)
print("These are the Odd number's :",ListOdd)