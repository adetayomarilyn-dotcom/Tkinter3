from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("200x200")
def msg():
    messagebox.showwarning("Alert", "Stop! Virus Detected")
btn = Button(root, text="Scan for virus", command=msg)
btn.place(x=50, y=50)
root.mainloop()


