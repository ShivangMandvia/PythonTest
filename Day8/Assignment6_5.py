#5>	Check a string is palindrome or not, using function and lambda function
def CheckPalindrome(i):
    l= len(str)
    for count in range(0, (l//2)):
        if(i[count] == i[l-1-count:l-count:1]):
            count+=1

    if(count == l//2):
        print("It's Palindrome")
    else:
        print("It's Not Palindrome")
str = input("Enter a String :")
CheckPalindrome(str)