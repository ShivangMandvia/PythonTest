class Name:
    def __init__(self,name,age):
        self.name =name
        self.age = age
    def des(self,name2,age2):
        name2 = input("ENter name - ")
        age2 = int(input("Enter age -"))
        return name2,age2

a = input("ENter name - ")
b = int(input("Enter age -"))

x = Name(a,b)

print(x.name)
print(x.age)
y =Name("jay",34)
print(y.des())
print(y.name2)
print(y.des(a,b))