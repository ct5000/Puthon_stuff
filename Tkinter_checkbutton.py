from Tkinter import *

def test():
    if var.get():
        print "Checked"
    else:
        print "Unchecked"

master = Tk()

var = IntVar()

c = Checkbutton(master, text="Color image", variable=var)
b = Button(master, text = "Test", command = test)
c.pack()
b.pack()

mainloop()
