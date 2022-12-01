#9> Write Python Program to Count the Occurrences of Each Word and Also Count the Number of Words.

n=input("Enter the text").split(" ")
for x in range(len(n)):
    print("The word ",n[x]," occurs ",n.count(n[x]),"time")
print("The total number of words in the text is:", len(n))