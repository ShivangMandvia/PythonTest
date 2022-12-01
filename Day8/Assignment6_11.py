#11>	Write a program to find odd and even number in range of n, using function and lambda function

def OddEvenList(List1,List2):
    for i in range(1, n+1):
        if i%2 == 0:
            List1.append(i)
        else:
            List2.append(i)

n =  int(input("Enter a Number : "))
ListEven =[]
ListOdd = []
OddEvenList(ListEven,ListOdd)
print("These are the Even number's :",ListEven)
print("These are the Odd number's :",ListOdd)