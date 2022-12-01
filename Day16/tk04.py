#Create Check Box
from tkinter import*

root = Tk()
root.title("Check Box")
root.geometry("100x100")

CheckVar1 = IntVar()
CheckVar2 = IntVar()


def Display():
    hi = CheckVar1.get()
    print(hi)

C1 = Checkbutton(root, text = "Music" , variable= CheckVar1, onvalue=1, offvalue=0, command = Display)
C2 = Checkbutton(root, text = "Video" , variable= CheckVar2, onvalue=1, offvalue=0)


C1.pack()
C2.pack()

root.mainloop()

