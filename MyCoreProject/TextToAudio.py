from tkinter import Tk,ttk,messagebox
from gtts import gTTS
import os
def Convert():
    mytext =entry.get()
    mytxt=str(mytext)
    language =cmb.get()
    myobj = gTTS(text=mytxt, lang=language, slow=False)
    mb = messagebox.showinfo("Text To Audio ", "MP3 File is Saved")
    myobj.save("yoursayings.mp3")
    os.system("mpg321 yoursayings.mp3")

window=Tk()
window.geometry('300x200')
entry=ttk.Entry(window ,width="30")
cmb=ttk.Combobox(window,width=20)
cmb['values']=("en","fr","Select language")
cmb.current(2)
btn=ttk.Button(window,text="Convert",command=Convert)
entry.pack()
cmb.pack()
btn.pack()
window.mainloop()