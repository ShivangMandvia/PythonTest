#Create a simple Pandas Series from a list:
import pandas as pd

# a = [1, 7, 2]
# x = pd.Series(a)
# print(x)

#Create your own labels:

a = [3.4,6.7,8.9]
x = pd.Series(a, index = ["x", "y", "z"])
print(x)

print(x["y"])