#8> Write Python Program to Reverse Each Word. 
class Rev:
    def Revstring(self,str):
        str1 =" "
        a =[]
        s= str.split(" ")
        for i in range(len(s)):
            p = s[i]
            a.append(p[::-1])
        return (str1.join(a))

x=input("Enter a sentence :\n")
tst = Rev()
y = tst.Revstring(x)
print(y)