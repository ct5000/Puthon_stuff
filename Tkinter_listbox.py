from Tkinter import *

def getValue():
    items = map(int, listbox.curselection())
    print listbox.get(items[0])

    
root = Tk()

listbox = Listbox(root)
listbox.pack()
variabler = ['v', 't', 's', 'a']


for item in variabler:
    listbox.insert(END, item)

b = Button(root, text = "test", command = getValue)
b.pack()
mainloop()
