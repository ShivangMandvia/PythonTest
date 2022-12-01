#numpy

import numpy as np

#One Dimensional(1D) array
a = np.array([1,2,3,4,5,6,7])

print(a)
print(type(a))
print(f"Dimen = {a.ndim}\n")


#two Dimensional(2D) array

a= np.array([[1,2,3],[4,5,6]])
print(a)
print(f"Dimen = {a.ndim}\n")

#3D Array
print("3D array is :\n")
a= np.array([[[1,2,3],[4,5,6],[7,8,9]]])
print(a)
print(f"Dimen = {a.ndim}\n")
