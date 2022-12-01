#2> Write a program to repeatedly check for the largest number until the user enters “done”

class HighNumber:
    def LargestInList(self,list1):
        while(1):
            out = input("Enter new value's or type 'done' to exit:")
            if(out == "done"):
                return list1[0]
                exit()
            a  = int(out)
            if(out != "done"):    
                if(len(list1)) == 0:
                    list1.append(a)
                    print(list1)            
                elif(len(list1)) == 1:
                    list1.append(a)
                    print(list1)
                elif(len(list1)) > 1:
                    list1.append(a)
                    list1.sort(reverse=True)
                    print(list1)
                    print(f"{list1[0]} is a largest number")
                    

tst = HighNumber()
lister = [15,56,59,45]
a = tst.LargestInList(lister)



    

    
