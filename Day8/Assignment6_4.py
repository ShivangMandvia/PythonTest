#4>	Check a number is Armstrong or not, using function and lambda function

def checkDigits(n):
    count=0
    temp = n
    while(temp>0):
        count+=1
        temp = temp//10
    return count

def CheckArmstrong(n,pow):
    a = lambda sum,num,pow:sum+num**pow
    total = 0
    tempo = n
    while tempo>0:
        n1 = tempo%10
        total = a(total,n1,pow) 
        tempo = int(tempo /10)

    if n == total:
        print(n,"is an armstrong number")
    else:
        print(n,"is not an armstrong number")



n1 =  int(input("Enter a Number : "))
power = checkDigits(n1)
CheckArmstrong(n1,power)

