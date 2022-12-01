#9> Write Python Program to Count the Occurrences of Each Word and Also Count the Number of Words.
class WordMani:
    def WordCount(self,str):
        lists = str.split(" ")
        for x in range(len(lists)):
            print("The word ",lists[x]," occurs ",lists.count(lists[x]),"time")
        print("The total number of words in the text is:", len(lists))        
        


n=input("Enter the text : ")
tst = WordMani()
tst.WordCount(n)