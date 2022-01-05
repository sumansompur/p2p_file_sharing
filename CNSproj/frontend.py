from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.geometry("600x400")
load = Image.open("bgphoto612x612.jpg")
render = ImageTk.PhotoImage(load)
img = Label(image=render)
img.place(x=0, y=0)
label = Label(root , text="Welcome To The Network!")
label.pack()
e= Entry(root)
e.pack()
e.insert(0,"Enter your IPaddress:")
button=Button(root,text="Submit")
button.pack()

root.mainloop()
