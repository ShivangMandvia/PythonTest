#2>	Print all prime number range – n.(for while).

#for loop
"""
n = int(input("Enter a Number: "))

for x in range(1, n):
    if(x>1):
        for i in range(2,x):
            if(x%i)==0:
                break
        else:
            print(x)

"""
#while loop

"""

a = 1
n = int(input("Enter a Number: "))
while(a <= n):
    count = 0
    i = 2
    while(i <= a//2):
        if(a % i == 0):
            count = count + 1
            break
        i = i + 1
    if (count == 0 and a!= 1):
        print(a)
    a+=1

"""