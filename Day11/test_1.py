#convert tuple to list/ list to tuple using lambda function
list1 = [23,"cdac","Kolkata"]

print(list1)

x = tuple(map(lambda b:b,list1))
print(x)