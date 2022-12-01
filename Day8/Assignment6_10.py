#10>	Write a program to show any multiplication table, using function and lambda function

def MultiplicationTable(n):
    for x in range(1,12):
        op = n*x
        print("%d x %d = %d" %(n,x,op))

num = int(input("Enter a number for table :"))
MultiplicationTable(num)
