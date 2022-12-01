#6. Write a program that accepts user input as a string and encrypts the input by adding and prints the encrypted message

n = input("Enter the String:")
estring1 = ""
for i in range(len(n)):
    encyrp = ord(n[i])
    estring2 = chr(encyrp+5)
    estring1 =estring1+estring2
print(estring1)

