#10>	Write a program to show any multiplication table.

n = int(input("Enter a number for table :"))

for x in range(1,13):
    op = n*x
    print("%d x %d = %d" %(n,x,op))