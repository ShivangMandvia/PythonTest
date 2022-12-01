# # # 
# # Program to add two matrices using nested loop
# # import numpy as np

# # # x= np.array([[]])
 
# # X = [[1,2,3],
# #     [4 ,5,6],
# #     [7 ,8,9]]
 
# # Y = [[9,8,7],
# #     [6,5,4],
# #     [3,2,1]]
 
 
# # result = [[0,0,0],
# #         [0,0,0],
# #         [0,0,0]]
 
# # # iterate through rows
# # for i in range(len(X)):  
# # # iterate through columns
# #     for j in range(len(X[0])):
# #         result[i][j] = X[i][j] + Y[i][j]
 
# # for r in result:
# #     print(r)
    
# ###################
# #
# # Program to add two



# ARNAB BISWAS DRAT14:38
# Write a program that accepts user input as a string and encrypts the input by adding 5
# and prints the encrypted message.
# CDAC Kolkata14:38
# just one min
# ARNAB BISWAS DRAT14:38
# ok sir
# CDAC Kolkata14:58
# Write a program that accepts user input as a string and encrypts the input by adding 5 and prints the encrypted message.
# 	A=1 ,B=2………..z=26
# i/p= ARNAB
#  a=i/p[0] (a=A)
# b= i/p[(x+1):]
# if(a==’A’):
#      x=(value of “A”) + 5
# 	if(X!=26) : x=X%26
# 	else : Z
#          check( Alpha bate name – value)
# 	l=list(append()) 
# 1+5 = 6
# Check 6==F
# o/p- f
# range(1):

# i/p = RNAB
# R = 
# ---- NAB
# Check ( R respected no == 20)
# Append()
# (Check OUR No(NO + 5) is > 21 –  no%26 = 
# o/p= fZ


# b= x
# z=a[x]
# CDAC Kolkata15:26
# # # 
# # Program to add two matrices using nested loop
# # import numpy as np

# # # x= np.array([[]])
 
# # X = [[1,2,3],
# #     [4 ,5,6],
# #     [7 ,8,9]]
 
# # Y = [[9,8,7],
# #     [6,5,4],
# #     [3,2,1]]
 
 
# # result = [[0,0,0],
# #         [0,0,0],
# #         [0,0,0]]
 
# # # iterate through rows
# # for i in range(len(X)):  
# # # iterate through columns
# #     for j in range(len(X[0])):
# #         result[i][j] = X[i][j] + Y[i][j]
 
# # for r in result:
# #     print(r)
    
# ###################
# #
# # Program to add two
# CDAC Kolkata15:29
# # #
# # # input two matrices of size n x m
# # matrix1 = [[12,7,3],
# #         [4 ,5,6],
# #         [7 ,8,9]]
# # matrix2 = [[5,8,1],
# #         [6,7,3],
# #         [4,5,9]]
 
# # res = [[0 for x in range(3)] for y in range(3)]
 
# # # explicit for loops
# # for i in range(len(matrix1)):
# #     for j in range(len(matrix2[0])):
# #         for k in range(len(matrix2)):
 
# #             # resulted matrix
# #             res[i][j] += matrix1[i][k] * matrix2[k][j]
# # print("Multiplication of two matrices = ") 
# # print (re
# CDAC Kolkata15:53
# pip install pandas
# CDAC Kolkata16:53
# pip install matplotlib
# CDAC Kolkata17:09
# # Scatter Plot

# import matplotlib.pyplot as plt
# import numpy as np

# x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
# y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])

# plt.scatter(x, y)
# plt.show()
# # Bar Plot
# import matplotlib.pyplot as plt
# import numpy as np

# x = np.array(["A", "B", "C", "D"])
# y = np.array([3, 8, 1, 10])

# plt.bar(x,y)
# plt.show()
# CDAC Kolkata17:11
# # The hist() function will read the array and produce a histogram
# import matplotlib.pyplot as plt
# import numpy as np

# x = np.random.normal(170, 10, 250)

# plt.hist(x)
# plt.show()
# #

# import matplotlib.pyplot as plt
# import numpy as np

# y = np.array([35, 25, 25, 15])

# plt.pie(y)
# plt.show()
# CDAC Kolkata17:12
# #
# # Import libraries
# import matplotlib.pyplot as plt
# import numpy as np
 
 
# # Creating dataset
# np.random.seed(10)
# data = np.array([12,34,56,78])
 
# fig = plt.figure(figsize =(10, 7))
 
# # Creating plot
# plt.boxplot(data)
 
# # show plot
# plt.show()
# import numpy as np
# import matplotlib.pyplot as plt
  
# # creating a list of 
# # uniformly distributed values
# uniform = np.arange(-100, 100)
  
# # creating a list of normally
# # distributed values
# normal = np.random.normal(size = 100)*30
  
# # creating figure and axes to
# # plot the image
# fig, (ax1, ax2) = plt.subplots(nrows = 1, 
#                                ncols = 2,
#                                figsize =(9, 4),
#                                sharey = True)
  
# # plotting violin plot for
# # unifo
# CDAC Kolkata17:23
# # Read A file
# f = open("demo01.txt", "r")
# print(f.read())
# #Open the file "demofile2.txt" and append content to the file:

# f = open("demo01.txt", "a")
# f.write("Hii I am AMALJIT")
# f.close()

# #open and read the file after the appending:
# f = open("demo01.txt", "r")
# print(f.read())
# #Create a file called "myfile.txt":

# f = open("myfile.txt", "x")

# #Create a new file if it does not exist:

# # f = open("myfile.txt", "w")
# # Check if file exists, then delete it:

# import os
# if os.path.exists("myfile.txt"):
#   os.remove("myfile.txt")
# else:
#   print("The file does not exist")
# Ashutosh Dhotre DRAT17:28
# Write Python program to sort words in a sentence in decreasing order of 
# their length. Display the sorted words along with their length