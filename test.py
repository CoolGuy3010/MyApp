from tk import *

root = Tk()

def Clicked():
    print("I was clicked")

m = Label(root,text="Hello")
m.pack()
b = Button(root,text="Click",command=Clicked)
b.pack()

root.mainloop()
