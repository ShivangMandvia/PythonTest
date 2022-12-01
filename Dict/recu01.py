# # Recursive function
# def factorial(n):
#   if n == 1:
#       return n
#   else:
#       return (n * factorial(n-1))
 
# # user input
# num = 2
 
# # check if the input is valid or not
# if num < 0:
#   print("Invalid input ! Please enter a positive number.")
# elif num == 0:
#   print("Factorial of number 0 is 1")
# else:
#   print(f"Factorial of number {num} is = ", factorial(num))
  
# x=3
# y=2  
  
# a=lambda x,y : (x>y)
# print(a(int(input("Enter the value 1 -")),int(input("Enter the value 2 - "))))

# lambda using if
x=3
y=6
a = lambda x,y : x if(x>y)  else y 

print(a(x,y))