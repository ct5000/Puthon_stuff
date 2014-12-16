from Tkinter import *

def hello():
    print "Hello World"

root = Tk()
frame = Frame(root)
frame.pack()

b = Button(root, text = "Hello", command = hello)
b2 =  Button(root, text = "Quit", command = frame.quit)
b2.pack()
b.pack()

root.mainloop()
root.destroy()
