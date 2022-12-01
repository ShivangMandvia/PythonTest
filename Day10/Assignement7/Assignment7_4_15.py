#5> Write a program to find the sum of digits of a number 


class Sumodig:
    def SumOfDigits(self, num):
        sum_digits = lambda number: 0 if number == 0 else (number % 10) + sum_digits (number // 10)
        return sum_digits(num)



a=int(input("Enter the number : "))
tst = Sumodig()
sum1 = tst.SumOfDigits(a)
print("The sum of digits of a number is: ",sum1)   


