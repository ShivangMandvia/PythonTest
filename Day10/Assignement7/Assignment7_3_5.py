#5>	Check a string is palindrome or not.

class StringMani():
    def stringPalincheck(self,str1):
        Strlength = len(str1)
        strrev = lambda x:1 if(x==x[::-1]) else 0
        checkpoint = strrev(str1)
        if(checkpoint == 1):
            print(f"The String '{str1}' is Palindrome")
        if(checkpoint == 0):
            print(f"The String '{str1}' is not Palindrome")


n = input("Enter a string: ")
test = StringMani()
test.stringPalincheck(n)



