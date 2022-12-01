from tkinter import *

r = Tk()

r.title("String Reversal")
r.geometry("300x300")

def main():
    lbl0 = Label(r, text= "Enter a text Below")
    lbl0.pack()
    E0= Entry(r, width = 40)
    E0.pack()
    E0.insert(0,"")
    B0 = Button(r, text="Display Reverse", command=lambda:rev(E0.get(),lbl1))
    B0.pack()
    lbl1 = Label(r)
    lbl1.pack()

def rev(str1,lbl1):
    str2 = str1[::-1]
    lbl1.config(text=str2)
    # lbl1=Label(r,text=str2)
    # lbl1.pack()
    

# r.mainloop()

if __name__ == "__main__":
    main()
    r.mainloop()
