#Create Entry

from tkinter import*

root =Tk()

#Creating Entry
entry1 =Entry(root, width=50)
entry1.pack()
entry1.insert(0, "Enter your name...")
entry2=Entry(root, width=100)
entry2.pack()

def save_data():
    hello = "Hello " + entry1.get()
    entry2.delete(0, END)
    entry2.insert(0, hello)
    # print(hello)
    # lbl1 = Label(root, text=hello)
    # lbl1.pack()

btn1 =Button(root, text="Save", command=save_data)
btn1.pack()
root.mainloop()
