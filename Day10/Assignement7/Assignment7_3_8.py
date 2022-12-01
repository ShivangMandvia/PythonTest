#8>	Input a tuple and reverse a string.

class TupleMnpltr:
    def TupleCreator(self,list2 ,num):
        for item in range(0,num):
            ListElement = input("Enter string at %d position of list :"%item) 
            list2.append(ListElement)
        return tuple(list2)
            
    def Display_Tuple(self,tup):
        l = len(tup)
        for i  in range(0,l):
            print(i, "->", tup[i])

    def StrReverseFromTuple(self,tup,position):
        list1 = list(tup)
        Str1 = list1[n]
        Str1 = Str1[::-1]
        list1[position] =Str1
        return tuple(list1)

n = int(input("Enter num of elements to create tuple :"))
tup1=[]
tst = TupleMnpltr()
t1 = tst.TupleCreator(tup1,n)
tst.Display_Tuple(t1)
n = int(input("Enter the number of Element to reverse string :"))
t1 = tst.StrReverseFromTuple(t1,n)
print("This is the Tuple is:",t1,end = "\n")


