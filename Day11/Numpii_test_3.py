#numpy
#Numpy in much more faster than List
import numpy as np

#One Dimensional(1D) array
a = np.array([1,2,3,4,5,6,7])

#Array copy
x=a.copy()
print(x)

# View Function
x = a.view()
print("View - ",x)

#Array Shape
a = np.array([1,2,3,4,5,6,7])
print(a.shape)

#(2D) array
a = np.array([[1,2,3],[4,5,6]])
print(a.shape)


#Access 2d array with for loop;

a = np.array([[1,2,3],[4,7,9]])

numRow, numCol = a.shape
for x in range(numRow):
    for y in range(numCol):
        # print(y)
        print(a[x][y])