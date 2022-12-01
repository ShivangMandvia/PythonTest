from tkinter import *

root = Tk()
root.geometry("300x300")


l1 = Label(root, text ="Registration form")
l1.place(x=10,y=20)


#Creating Entry
entry1 =Entry(root, width=50)
entry1.place(x=10,y=40)

entry1.insert(0, "Remove this and Enter your name...")

entry2 =Entry(root, width=50)
entry2.place(x=10,y=60)

entry2.insert(0, "Remove this and Enter your age...")

radioVar = IntVar()


    

r1 = Radiobutton(root, text="MALE", variable=radioVar, value=1)
r1.place(x= 10,y= 80)
r2 = Radiobutton(root, text="FEMALE", variable=radioVar, value=2)
r2.place(x= 80,y= 80)

def save_data():
    
    name = entry1.get()
    age = entry2.get()
    selected = {
        1: "Male",
        2: "Female"
    } 
    print(f"Name :{name}" ,end ="\n")
    print(f"Age :{age}",end ="\n")
    print(f"Gender :{selected[radioVar.get()]}",end ="\n")



btn1 =Button(root, text="Save", command=save_data)
btn1.place(x=120,y=200)

root.mainloop()