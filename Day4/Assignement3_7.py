#7>	Input a list and reverse a string.
n = int(input("Enter Number of Elements for List: "))
list1 = []

for item in range(0,n):
    print("Enter the element no.", item," :")
    ListElement = input()
    print(item)
    #list1[item] = ListElement  
    list1.append(ListElement)

print(len(list1))
print(list1)

print("Now, lets reverse a string ")
strnum = int(input("Enter the element to edit the string :"))
if (strnum <len(list1) and strnum >-1):
    print("Inside")
    str1 = list1[strnum]
    print(str1)
    str1 = str1[::-1]
    list1[strnum] =str1

print("Updated list : ",list1)