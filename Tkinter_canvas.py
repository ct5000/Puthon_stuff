from Tkinter import *

root = Tk()

def test(event):
    if event.x < 200 and event.x > 150 and event.y > 150 and event.y < 200:
        print "Hello"
    elif event.x < 100 and event.x > 50 and event.y > 50 and event.y < 100:
        print "Spam"

def simple():
    print 2 + 2

w = Canvas(root, width = 300, height = 300)
w.pack()
w.create_rectangle(150, 150, 200, 200, fill = "red")
w.create_rectangle(50, 50, 100, 100, fill = "blue")

b = Button(root, text = "simple", command = simple, width = 5)
b2 = Button(root, text = "quit", command = w.quit)
j = w.create_window(130, 150, window = b)
b2.pack()

w.bind("<Button-1>", test)


mainloop()
root.destroy()
