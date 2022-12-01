#12> Write a program to find odd and even number between any range, using function and lambda function

def OddEvenList(F,L,List1,List2):
    for i in range(F, L+1):
        if i%2 == 0:
            List1.append(i)
        else:
            List2.append(i)

FirstNumber =  int(input("Enter  First Number : "))
LastNumber =  int(input("Enter  Last Number : "))
ListEven =[]
ListOdd = []
OddEvenList(FirstNumber,LastNumber,ListEven,ListOdd)
print("These are the Even number's :",ListEven)
print("These are the Odd number's :",ListOdd)

