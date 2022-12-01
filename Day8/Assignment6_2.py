#2>	Print all prime number range – n.(for while), using function and lambda function

def PrimeRange(n):
    for x in range(1, n):
        if(x>1):
            for i in range(2,x):
                if(x%i)==0:
                    break
            else:
                print(x)
    

n1 = int(input("Enter a Number: "))
PrimeRange(n1)


