#1> Write a NumPy program to test whether none of the elements of a given array is zero.

import numpy as np

class NumPPy:
    def findZero(self,a):
        for i in range(len(a)):
            if(a[i] == 0):
                return False
        return True
        #return a.all()
def main():
    a1 = np.array([1, 15, 0, 48, 15, 20, 35, 41, 18, 16])
    test = NumPPy()
    if(test.findZero(a1)):
        print("It doest have any element as Zero")
    else:
        print("It does have elements as Zero")
if __name__ =="__main__":
    main()
