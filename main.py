import tkinter
import ctypes

w=tkinter.Tk()
ctypes.windll.shcore.SetProcessDpiAwareness(2)

w.title("IMAGE EDITOR-WOC-4.0")
w.geometry('1420x720')
w.configure(bg="#000000")

img=tkinter.Canvas(w, width=1100,height=600,bg="Grey")
img.grid(column=0,row=0,columnspan=10)

open=tkinter.Button(w,text='Open',width=5,padx=15,pady=10,bg="GREY",fg="White",font='Arial')
open.grid(column=12,row=0,padx=5,pady=5,sticky="N")

save=tkinter.Button(w,text='Save',width=5,padx=15,pady=10,bg="GREY",fg="White",font='Arial')
save.grid(column=13,row=0,padx=10,pady=5,sticky="N")

Crop=tkinter.Button(w,text='Crop',width=5,padx=5,pady=10,bg="GREY",fg="White",font='Arial')
Crop.grid(column=0,row=2,padx=5,pady=5,sticky="W")

BW=tkinter.Button(w,text='Black and White',width=15,padx=5,pady=10,bg="GREY",fg="White",font='Arial')
BW.grid(column=1,row=2,padx=5,pady=5,sticky="W")

ic=tkinter.Button(w,text='Invert Colour',width=15,padx=5,pady=10,bg="GREY",fg="White",font='Arial')
ic.grid(column=2,row=2,padx=5,pady=5,sticky="W")


hf=tkinter.Button(w,text='Horizontal flip',width=15,padx=5,pady=10,bg="GREY",fg="White",font='Arial')
hf.grid(column=3,row=2,padx=5,pady=5,sticky="W")

vf=tkinter.Button(w,text='Vertical flip',width=15,padx=5,pady=10,bg="GREY",fg="White",font='Arial')
vf.grid(column=4,row=2,padx=5,pady=5,sticky="W")

rl=tkinter.Button(w,text='Rotate Left ⟳',width=15,padx=5,pady=10,bg="GREY",fg="White",font='Arial')
rl.grid(column=5,row=2,padx=5,pady=5,sticky="W")

rr=tkinter.Button(w,text='Rotate Right ⟳',width=15,padx=5,pady=10,bg="GREY",fg="White",font='Arial')
rr.grid(column=6,row=2,padx=5,pady=5,sticky="W")



w.mainloop()