#Load the CSV into a DataFrame:

import pandas as pd

# x = pd.read_csv(r'C:\Users\dell\Desktop\TCP_IP\Iris.csv')
x= pd.read_excel("Book1.xlsx")
#x= pd.read()
# print(df)

# print(df.to_string()) 

# print(df)
print(x.head())                # tail()
# print(x.tail(10)) 



# # Print information about the data:
# print(df.info()) 