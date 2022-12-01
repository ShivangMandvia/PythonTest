#12>Write a program to find odd and even number between any range

FirstNumber =  int(input("Enter  First Number : "))
LastNumber =  int(input("Enter  Last Number : "))
ListEven =[]
ListOdd = []

for i in range(FirstNumber, LastNumber+1):
    if i%2 == 0:
        ListEven.append(i)
    else:
        ListOdd.append(i)

print("These are the Even number's :",ListEven)
print("These are the Odd number's :",ListOdd)