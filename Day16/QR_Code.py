import pyqrcode as qr #pip3 install pyqrcode for Ubuntu 
from tkinter import *
from tkinter.filedialog import*

#Initial Main window

root = Tk()
root.geometry("500x500")
root.title("QR code Generator")
root.iconbitmap("C:\\Users\Mitt\Desktop\Python\Day16\qricon.ico")

#Global Variables

linkOrText = StringVar()

#Create functions

def code_generator():
    string1 = linkOrText.get()
    url_txt = qr.create(string1)
    path_save = asksaveasfilename()
    url_txt.png(path_save+"QRCode.png")


def main():
    lbl0 = Label(root, text= "Enter link or text:", width=20, font= ("arial",10, "bold"))
    lbl0.pack()
    ent0 = Entry(root, textvar=linkOrText)
    ent0.pack()
    btn0 = Button(root, text="Generate QR code", command=code_generator)
    btn0.pack()
    btn1 = Button(root,text= "Exit", command= root.quit)
    btn1.pack()

if __name__ == "__main__":
    main()
    root.mainloop()



