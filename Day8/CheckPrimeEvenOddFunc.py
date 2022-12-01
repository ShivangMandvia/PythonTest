def isPrime(x):
    count=0
    if(x<1):
        print("Wrong Input")
    else:
        for i in range(2,x):
            if(x%i==0):
                count=count+1
                break
        if(count!=0)or(x<2):
            print("The number is not prime.")
        elif(count==0)or(x==2):
            print("The number is prime.")

def CheckEvenOdd(x):
    if(x%2==0):
        print("The Number is Even")
    else:
        print("The Number is Odd")

n = int(input("Enter a number: "))
isPrime(n)
CheckEvenOdd(12)
