#3>	Check a number is odd or even. using function and lambda function

def CheckEvenOdd(x):
    if(x%2==0):
        print("The Number is Even")
    else:
        print("The Number is Odd")

n = int(input("Enter a number: "))
CheckEvenOdd(n)