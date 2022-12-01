#2. Write a program to print ASCII values from A to Z and z to a.

a = "A"
print("The ASCII value of A-Z is :")
for x in range(ord(a),ord(a)+26):
    print(chr(x),"-",x)

a = "a"
print("The ASCII value of a-z is :")
for x in range(ord(a),ord(a)+26):
    print(chr(x),"-",x)