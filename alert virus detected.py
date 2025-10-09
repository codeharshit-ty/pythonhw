from tkinter import*
from tkinter import messagebox
root = Tk()
root.geometry("200x200")
def msg():
    messagebox.showwarning("Alert","Stop! Virus Found.")
Button = Button(root,text= "Scan for Virus",command=msg)
Button.place(x=40,y=40)
root.mainloop()