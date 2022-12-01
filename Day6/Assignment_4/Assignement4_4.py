#4> Discuss the int(), float(), str(), chr() and complex() type conversion functions with examples.

# Discuss the int, float, str, chr and complex type conversion
# integer to float
from sys import int_info


a=10
print("a:",a)
print("The orig type of a is :",type(a))
a=float(a)
print("a:",a)
print("The changed type of a is :",type(a))

# integer to string
a=10
print("a:",a)
print("The orig type of a is :",type(a))
a=str(a)
print("a:",a)
print("The changed type of a is :",type(a))

# integer to complex
a=10
print("a:",a)
print("The orig type of a is :",type(a))
a=complex(a)
print("a:",a)
print("The changed type of a is :",type(a))

# integer to boolean

a=10
print("a:",a)
print("The orig type of a is :",type(a))
a=bool(a)
print("a:",a)
print("The changed type of a is :",type(a))

# float to string
a=10.5
print("a:",a)
print("The orig type of a is :",type(a))
a=str(a)
print("a:",a)
print("The changed type of a is :",type(a))

# float to complex
a=10.5
print("a:",a)
print("The orig type of a is :",type(a))
a=complex(a)
print("a:",a)
print("The changed type of a is :",type(a))

# Float to boolean
a=10.5
print("a:",a)
print("The orig type of a is :",type(a))
a=bool(a)
print("a:",a)
print("The changed type of a is :",type(a))

# Float to integer

a=10.5
print("a:",a)
print("The orig type of a is :",type(a))
a=int(a)
print("a:",a)
print("The changed type of a is :",type(a))

# String to float
a="10"
print("a:",a)
print("The orig type of a is :",type(a))
a=float(a)
print("a:",a)
print("The changed type of a is :",type(a))

# String to integer
a="10"
print("a:",a)
print("The orig type of a is :",type(a))
a=int(a)
print("a:",a)
print("The changed type of a is :",type(a))

# String to complex
a="10"
print("a:",a)
print("The orig type of a is :",type(a))
a=complex(a)
print("a:",a)
print("The changed type of a is :",type(a))

# String to boolean

a="10"
print("a:",a)
print("The orig type of a is :",type(a))
a=bool(a)
print("a:",a)
print("The changed type of a is :",type(a))



# complex to string
a=10+5j
print("a:",a)
print("The orig type of a is :",type(a))
a=str(a)
print("a:",a)
print("The changed type of a is :",type(a))


# complex to boolean

a=10+5j
print("a:",a)
print("The orig type of a is :",type(a))
a=bool(a)
print("a:",a)
print("The changed type of a is :",type(a))

# boolean to float
a=True
print("a:",a)
print("The orig type of a is :",type(a))
a=float(a)
print("a:",a)
print("The changed type of a is :",type(a))

# boolean to string
a=True
print("a:",a)
print("The orig type of a is :",type(a))
a=str(a)
print("a:",a)
print("The changed type of a is :",type(a))

# boolean to complex
a=True
print("a:",a)
print("The orig type of a is :",type(a))
a=complex(a)
print("a:",a)
print("The changed type of a is :",type(a))

# boolean to integer

a=True
print("a:",a)
print("The orig type of a is :",type(a))
a=int(a)
print("a:",a)
print("The changed type of a is :",type(a))