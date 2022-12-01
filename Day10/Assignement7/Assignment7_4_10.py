#10> Write Python Program to Find the Longest Word in a sentence , input from user end . 

class StringLong:
    def longCheck(self,b):
        x = b.split(" ")
        x.sort(reverse=True, key=len)
        print("The longest word in the text is:",x[0])
        
a=input("Enter the text:")
tst = StringLong()
tst.longCheck(a)
    
