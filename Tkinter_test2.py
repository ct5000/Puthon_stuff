from Tkinter import *

def button1():
    print "This is the first button"

def quitfunc():
    root.destroy()

root = Tk()
frame = Frame(root, width = 200, height = 200)
frame.pack_propagate(0)
frame.pack()
b = Button(frame, text = "Button1", command = button1)
quitb = Button(frame, text = "Quit", command = quitfunc)
b.pack(fill = BOTH, expand = 1)
quitb.pack(fill = BOTH, expand = 1)
root.mainloop()
frame.mainloop()
