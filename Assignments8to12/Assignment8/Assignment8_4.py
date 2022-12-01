"""
4> Write a NumPy program to test whether two arrays are element-wise
equal within a tolerance.
"""

import numpy as np
print("Test if two arrays are element-wise equal within a tolerance:")
print(np.allclose([1e10,1e-7], [1.000000000001e10,1e-7]))
