#2> Write a program to repeatedly check for the largest number until the user enters “done”

list1=[]
out = "a"
count = 0
while(1):
    out = input("Enter value's or type 'done' to exit:")
    if(out == "done"):
        exit()
    a  = int(out)
    if(len(list1) == 0):
        print("Enter a new value again :")
        list1.append(a)
    elif(len(list1) == 1):
        print("Enter a new value again :")
        list1.append(a)
    else:
        for x in range(0,len(list1)):
           if(a>list1[x]):
                count+=1
        if(count>=len(list1)):
            count = 0
            list1.append(a)
            print(a ,"is the largest number")
            
        else:
            list1.append(a)
            count+=1
            

    
