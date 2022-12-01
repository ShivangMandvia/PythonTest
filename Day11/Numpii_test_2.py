#numpy

import numpy as np

#One Dimensional(1D) array
a = np.array([1,2,3,4,5,6,7])

print(a)
print("result - ",a[1]+a[3])
print(f"Dimen = {a.ndim}\n")
#a[Starting Address : Ending Address: Skipping value]
print(a[::2])

b = np.array([ 23 , 56, "CDAC" , "KOLKATA" ])
print(b[0] + b[1])



#Numpy Array should have all elements of same datatype
c = np.array([ 23 , 56, 89 , 90 ])
print(c[0] + c[1])