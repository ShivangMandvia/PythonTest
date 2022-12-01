# Write a NumPy program to find common values between two
# arrays.
# Expected Output:
# Array1: [ 0 10 20 40 60]
# Array2: [10, 30, 40]
# Common values between two arrays:
# [10 40]

import numpy as np
a1 = np.array([0,10,20,40,60])
a2 = np.array([10,30,40])
l = []
for i in range(len(a1)):
    for j in range(len(a2)):
        if (a1[i] == a2[j]):
            l.append(a1[i])
print(a1)
print(list(a2))
print("Common values between two arrays:", end = "\n")
print(np.array(l))
print(dir(a1))