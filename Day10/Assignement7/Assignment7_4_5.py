#5> Write a Program to Prompt for a Score between 0.0 and 1.0. If the Score is out of range, print an error. If the score is between 0.0 and 1.0, print a grade using the following table

n=float(input("Enter the Score : "))
if(n<0.6)and(n>0):
    print("F")
elif(n>=0.6)and(n<0.7):
    print("D")
elif(n>=0.7)and(n<0.8):
    print("C")
elif(n>=0.8)and(n<0.9):
    print("B")
elif(n>=0.9)and(n<1):
    print("A")
else:
    print("Score is out of range.")