#2> Write a NumPy program to test whether any of the elements of a given array is non-zero.

import numpy as np

class NumPPy:
    def findNonZero(self,a):
        for i in range(len(a)):
            if(a[i] != 0):
                return False
        return True
        #return np.any(a)


def main():
    a1 = np.array([0, 0, 0, 0])
    test = NumPPy()
    if(test.findNonZero(a1)):
        print("It doesnt have any element as Non-Zero")
    else:
        print("It does have elements as Non-Zero")
if __name__ =="__main__":
    main()

