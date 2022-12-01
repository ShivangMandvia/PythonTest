#6>	Print First 10 numbers using for and while, using function and lambda function

def forFirstN_Element(a):
    print("For Loop")
    for x in range(1,a+1):
        print(x)

def whileFirstN_Element(a):
    i = 1
    print("While Loop")
    while(i<=a):
        print(i)
        i+=1
num = int(input("Enter a number :"))
forFirstN_Element(num)
whileFirstN_Element(num)






