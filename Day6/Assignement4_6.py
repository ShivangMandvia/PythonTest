#6> Explain the following list methods with an example. a) append() b) extend() c) insert() d) index() e) sort()

# Examples based on list methods
list1=["hi","one",2,"Three",4]
print("Origional list")
print(list1)
list1.append("CDAC")
print("Appended list with item (CDAC)")
print(list1)

list2=["Jai","viru"]
print("Extension list")
print(list2)
list1.extend(list2)
print("Updated list")
print(list1)

list1.insert(1, "Zen")
print("List with updated Zen")
print(list1)

print("The index of Three is",list1.index("Three"))
print("Sorted list")

list3=["JAI","OM","Jagdish"]
print(list3)
list3.sort()
print("Sorted list")
print(list3)
