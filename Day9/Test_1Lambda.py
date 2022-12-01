#METHOD1
def FindEvenInList(list1):
    list2 =[]
    for x in range(len(list1)):
        if(list1[x]%2==0):
            list2.append(list1[x]) 
    return list2

l = [2,6,3,9,5,8]
l2 = FindEvenInList(l)
print(l2)

#METHOD2
l = [2,6,3,9,5,8]
a = lambda x:print(x) if(x%2==0) else None
for i in range(len(l)):
    a(l[i])

#METHOD3---Most efficient
###VVIP
#learn about .format AND f"{} ---"
a = [2,6,3,9,5,8]
x = list(filter(lambda a :(a%2==0), a))
print("The new list is {}".format(x))


#METHOD4
# Use if-else in Lambda Functions
# check if number is even or odd
result = lambda x : f"{x} is even" if x %2==0 else f"{x} is odd"
# print for numbers
print(result(12))
print(result(11))


#SIR ka code

# Lambda Function
# SYNTAX - lambda ARg : EXPRESSION

# x = lambda a,b: a+b
# # x is not a variable......   x is a function which contains same number of parameter as the lambda function 


# z= x(2,4)

# print("Addition of two number using lambda function - ", x(2,4))

# normal function

# x=0
# y=0
# print("Result = ", add(x,y))


# def add(a,b):
#     a= int(input("Enter fst number - "))
#     b= int(input("Enter secnd number - "))
#     return(a+b)



# Simple lambda function
# Find even num