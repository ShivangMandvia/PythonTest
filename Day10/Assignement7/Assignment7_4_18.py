#18> Write a program to find the sum of any five integers. 

class Sumo:
    def SumOfFive(self):
        list1 = []
        for i in range(0,5):
            n = int(input(f"Enter number {i+1} : "))
            list1.append(n)
        return sum(list1)

tst = Sumo()
Total = tst.SumOfFive()
print(Total)