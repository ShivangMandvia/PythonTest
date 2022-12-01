#Create a simple Pandas Series from a dictionary:

# import pandas as pd
# dictionary01 = {"day1": 420, "day2": 380, "day3": 390}
# x = pd.Series(dictionary01)

# print(x)


# #Create a DataFrame from two Series:

import pandas as pd

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}
x = pd.DataFrame(data)
print(x)


#Return row 0:
#refer to the row index:
print(x.loc[0])

#Return row 0 and 1:
#use a list of indexes:
print(x.loc[[0, 1]])
