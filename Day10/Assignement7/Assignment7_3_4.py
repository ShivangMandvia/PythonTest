#4>	Check a number is Armstrong or not.

class Armstrong:
    def ArmstrongCheck(self,num):
        n = num
        count_digit = lambda number: 0 if number == 0 else 1 + count_digit(number//10)
        sumup = 0
        digits = count_digit(num)
        sum_digits = lambda number: 0 if number == 0 else ((number % 10)**digits) + sum_digits (number // 10)
        if(n==sum_digits(n)):
            print(f"{n} is an Armstrong Number")
        else:
            print(f"{n} is not an Armstrong Number")

num1 = int(input("Enter a number : "))
test = Armstrong()
test.ArmstrongCheck(num1)



