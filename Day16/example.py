from tkinter import *

root = Tk()

def click():
    var1, var2, var3, var4,var5 = 5,6,7,8,9
    
    lbl1.config(text=var1)
    lbl2.config(text=var2)
    lbl3.config(text=var3)
    lbl4.config(text=var4)
    lbl5.config(text=var5)
    
lbl1 = Label(root)
lbl1.pack()
lbl2 = Label(root)
lbl2.pack()
lbl3 = Label(root)
lbl3.pack()
lbl4 = Label(root)
lbl4.pack()
lbl5 = Label(root)
lbl5.pack()

btn = Button(root, text="Save", command=click)
btn.pack()

root.mainloop()