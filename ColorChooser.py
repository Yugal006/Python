from tkinter import *
from tkinter import colorchooser


def click():
    color = colorchooser.askcolor()
    colorHex = color[1]
    window.config(bg=colorHex)

window = Tk()
window.geometry("200x100")
button = Button (text="Click me" ,command=click)
button.pack()
close = Button (text="Exit" ,command=window.destroy)
close.pack()
window.mainloop()
