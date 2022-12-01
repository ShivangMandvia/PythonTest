#For Loop/ While Loop/ Nested Loops

#Testing For loop

# print("the - ", range(6))
# for x in range(1,6,2):
#     print(x)
#     continue
#     if x == 3:
#         break

#l1 = ["C" ,263, 4165 ,"Fsd", 78, 78,78]

# for x in l1:
#     print(x)

# for x in range(len(l1)):
#     print(l1[x])


#replication code for .count(argv) class  

# c=0
# for x in l1:
#     if(x == 78):
#         c+=1

# print("Value - ", c)

#OR

# c=0
# for x in l1:
#     if(x == 78):
#         c+=1
#     print("Value - ", c)


#Prime Number  logic


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

#___________ While Loop ___________#

# count = 0 
# while(count<5):
#     count+=1
#     print("CDAC") 

#------Prime number with While Loop-----#


# a = int(input("Enter the last number -"))
# i=2
# check = 2
# while(check<=a):
#     if(check%i == 0):
#         print(check)
#         if()
        
