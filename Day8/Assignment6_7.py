#7>	Input a list and reverse a string, using function and lambda function

def listCreator(list2 ,num):
    for item in range(0,num):
        ListElement = input("Enter string at %d position of list :"%item) 
        list2.append(ListElement)

def Display_list(list2):
    l = len(list2)
    for i  in range(0,l):
        print(i, "->", list2[i])

def StrReverseFromList(list2,position):
    temp = list2[position]
    Str1 = temp[::-1]
    list2[position] =  Str1
    

n = int(input("Enter num of elements to create list :"))
list1=[]
listCreator(list1,n)
Display_list(list1)
select = int(input("Enter element no to reverse :")) 
StrReverseFromList(list1,select)
print(list1)
