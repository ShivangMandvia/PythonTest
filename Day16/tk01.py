#Ubuntu
# sudo apt install python3-pip
# sudo apt install python- tk
# 

from tkinter import *

root = Tk()
root.title("PG_DRAT-GUI")
root.geometry("300x400")

#Creating a label wdget
myLabel1 = Label(root, text="PG-DRAT1")
myLabel2 = Label(root, text="PG-DRAT2")
myLabel3 = Label(root, text="PG-DRAT3")
myLabel4 = Label(root, text="PG-DRAT4")
myLabel5 = Label(root, text="PG-DRAT5")

# myLabel1.pack()
# myLabel2.pack()
# myLabel3.pack()
# myLabel4.pack()
# myLabel5.pack()

# #Bind the wigdet to main window
# myLabel1.grid(row =0,column=0)
# myLabel2.grid(row =1,column=1)
# myLabel3.grid(row =2,column=2)
# myLabel4.grid(row =3,column=3)
# myLabel5.grid(row =4,column=4)


#Bind the wigdet to main window
myLabel1.place(x=10,y=20)
myLabel2.place(x=100 , y=100)
myLabel3.place(x =200,y=200)
myLabel4.place(x =150,y=200)
myLabel5.place(x =40,y=40)

root.mainloop()