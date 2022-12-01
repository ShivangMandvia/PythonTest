#8>	Input a tuple and reverse a string.

x = ('apple', 'banana', 'cherry')
print("this is the tuple :",x)
n = int(input("Enter the number of Element to reverse string :"))
listx = list(x)

Str1 = x[n]
Str1 = Str1[::-1]
listx[n] =Str1

x = tuple(listx)
print(x)
