#op -l=["CDAC", "sourav" , "arnab", "kunal", "PUNE", "amaljith"] 
l=["amaljith", "sourav" , "arnab", "kunal", "amaljith","sourav"]
temp = []
count = 0
for x  in range(len(l)):
    #print(l[x])
    if(l[x] == "sourav"):
        temp.insert(x+count,"CDAC")  
        temp.append(l[x])
        count = count +1
    elif(l[x] == "amaljith"):
        temp.insert(x+count,"PUNE")          
        temp.append(l[x])
        count = count +1
    else:
        temp.append(l[x])
print(temp)        
