#4>	Check a number is Armstrong or not.

n =  int(input("Enter a Number : "))

total = 0

tempo = n
while tempo>0:
    n1 = tempo%10
    total+= n1 ** 3
    tempo = int(tempo /10)

if n == total:
    print(n,"is an armstrong number")
else:
    print(n,"is not an armstrong number")
