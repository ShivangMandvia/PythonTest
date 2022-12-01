#8> Write Python Program to Reverse Each Word. 
a = "hi"
x = []
x=input("Enter a sentence :\n").split(" ")
#x.sort(key=len)
for i in range(len(x)):
    a= x[i]
    print((a[::-1]), end= " ")