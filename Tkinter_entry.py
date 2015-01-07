from Tkinter import *

def getValue():
    num1 = int(e1.get())
    num2 = int(e2.get())
    print num1 + num2

root = Tk()

v1 = StringVar()
v2 = StringVar()
e1 = Entry(root, textvariable = v1)
e2 = Entry(root, textvariable = v2)

b = Button(root, command = getValue, text="Test")
e1.pack()
e2.pack()
b.pack()
v1.set("Tal 1")
v2.set("Tal 2")



root.mainloop()
