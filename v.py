from tkinter import *
from tkinter import filedialog
import os


# my function to load file
def callback():
    root.filename = filedialog.askopenfilename(initialdir="/", title="Select file",
                                               filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))
    v.set(str(root.filename))


# initialize my window
root = Tk()
global v
root.title("Dimo")
root.minsize(490, 500)
root.geometry("490x500")

# top frame
topFrame = Frame(root)
topFrame.pack()

# bottom frame
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

v = StringVar()



# my widgets
welcome = Label(topFrame, text="Welcome to IDS")
b1 = Button(topFrame, text="Load File", command=callback)
b2 = Button(bottomFrame, text="Start")
fileName = Label(topFrame, textvariable=v)
filedir = Label(root, text="File Directory")
img = PhotoImage(file="12.gif")
panel = Label(topFrame, image=img)
panel.pack(side="top", fill="both", expand="yes")

welcome.pack()
b1.pack()
b2.pack()
fileName.pack()


root.mainloop()
