from Tkinter import *

def test():
    print type(w.get())

master = Tk()

w = Spinbox(master, from_=0, to=10)
w.pack()

b = Button(master, text = "Test", command = test)
b.pack()

mainloop()
