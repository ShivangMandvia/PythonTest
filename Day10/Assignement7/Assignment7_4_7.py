#Write Python program to sort words in a sentence in decreasing order of their length. Display the sorted words along with their length. 

class StringSorter:
    def Sortup(self, y):
        x=y.split(" ")
        x.sort(key=len)
        for i in range(len(x)):
            print(x[i],"-",len(x[i]), end= " ")



tst = StringSorter()
x=input("Enter a sentence :\n") 
tst.Sortup(x) 