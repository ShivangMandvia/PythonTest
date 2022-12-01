#1>	Print all prime number between a range ( for, while), using function and lambda function

def PrimeforRange(a,b): 

    for x in range(a,b+1):
        if(x>1):
            for i in range(2,x):
                if(x%i == 0):
                    break
            else:
                print(x,end = '\n')



def PrimeWhile(a,b):
    while(a <= b):
        check = False
        i = 2
        while(i <= a//2):
            if(a % i == 0):
                check = True
                break
            i = i + 1
        if (check == False and a!= 1):
            print(a,"\t", end = '')
        a += 1



n1 = int(input("Enter the starting number -"))
n2 = int(input("Enter the Last number -"))

PrimeforRange(n1,n2)
PrimeWhile(n1,n2)

"""
a = lambda x,y: x+y
print(a(int(input("Enter a value :")),int(input("Enter a value :"))))

"""
