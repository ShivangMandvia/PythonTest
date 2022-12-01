#5>	Check a string is palindrome or not.

i = str(input("Insert : "))
l = len(i)
count = 0

for count in range(0, (l//2)):
    # print("i[count] :",i[count])
    # print("i[l-1-count:l-count:1]",i[l-1-count:l-count:1])
    if(i[count] == i[l-1-count:l-count:1]):
        count+=1

if(count == l//2):
#    print("Count no :",count)
    print("It's Palindrome")
else:
#    print("Count no :",count)
    print("It's Not Palindrome")