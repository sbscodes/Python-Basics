from tkinter import *
from tkinter import messagebox,ttk
top = Tk()
C = Canvas(top, bg="blue", height=250, width=300)
filename = PhotoImage(file = "C:\\Users\\Satish\\ui.PNG")
background_label = Label(top, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
entry=ttk.Entry(top)
C.pack()
entry.place(x=20 ,y=30)
top.mainloop()