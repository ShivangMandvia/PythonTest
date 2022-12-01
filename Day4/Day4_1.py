#String /LIST reversal without for loop
l1 = ["CDAC", 90 ,"KOLKATA"]

a= l1[2]

# a is string now
#a =a[start:stop:++/--]

a = a[ : :-1]
print(a)
print(dir(a))