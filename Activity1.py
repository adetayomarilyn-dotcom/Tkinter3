from tkinter import *
window = Tk()
window.title("Event Handler")
window.geometry("100x100")
def keypress(event):
    print("Key pressed:", event.char)
window.bind("<Key>", keypress)
def handle_click(event):
    print("The button was clicked")
btn = Button(window, text="Click Me")
btn.bind("<Button-1>", handle_click)
btn.pack()
window.mainloop()