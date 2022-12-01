#7>	Input a list and reverse a string.

class ListManipulator:
    def listCreator(self,list2,num):
        for item in range(0,num):
            ListElement = input("Enter string at %d position of list :"%item) 
            list2.append(ListElement)  
            #return list2  

    def StrReverseFromList(self,list2,position):
        strRev = list2[position]
        strRev = strRev[::-1]
        list2[position] = strRev
        #return list2

    def Display_list(self,list2):
        l = len(list2)
        for i  in range(0,l):
            print(i, "->", list2[i])
        #return list2

listInMain =[]
num = int(input("Enter number of elements you want in list: "))
tst = ListManipulator()
tst.listCreator(listInMain,num)
tst.Display_list(listInMain)
num = int(input("Enter position number of elements you want to reverse: "))
tst.StrReverseFromList(listInMain,1)
tst.Display_list(listInMain)
