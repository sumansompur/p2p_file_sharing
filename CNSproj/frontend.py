from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.geometry("1200x700")
load = Image.open("Network-Monitoring.jpg")
render = ImageTk.PhotoImage(load)
img = Label(image=render)
img.place(x=0, y=0)
label = Label(root , text="Welcome To The Network!",width=100)
label.pack(pady=50)
e= Entry(root,width=100)
e.pack(pady=50)
e.insert(0,"Enter your IPaddress:")
button=Button(root,text="Submit",width=30)
button.pack()

root.mainloop()
