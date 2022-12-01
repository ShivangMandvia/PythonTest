#16> Write a program to find the first n numbers in a Fibonacci series


class Fibo:
    def fibonacci(self,count):
        fib_list = [0, 1]
        any(map(lambda x: fib_list.append(fib_list[-1]+fib_list[-2]),range(2, count)))
        return fib_list
  

list1 = []
tst = Fibo()
num = int(input("Enter a number for fibonacci range: "))
list1 = tst.fibonacci(num)
print(list1)