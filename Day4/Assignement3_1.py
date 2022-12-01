#1>	Print all prime number between a range ( for, while).

#for loop based prime number from and to
"""
a = int(input("Enter the starting number -"))
b = int(input("Enter the Last number -"))
i = 1
for x in range(a,b+1):
    if(x>1):
        for i in range(2,x):
            if(x%i == 0):
                break
        else:
            print(x)
"""

#while loop based prime number from and to

"""

a = int(input("Enter the starting number -"))
b = int(input("Enter the Last number -"))
 
while(a <= b):
    check = False
    i = 2
    while(i <= a//2):
        if(a % i == 0):
            check = True
            break
        i = i + 1
    if (check == False and a!= 1):
        print(" %d" %a, end = '  ')
    a += 1

"""
