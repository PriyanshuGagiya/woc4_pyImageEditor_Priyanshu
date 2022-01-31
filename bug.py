from cProfile import label
from tkinter import *
import tkinter
import tkinter.filedialog 
from tkinter.ttk import *
from PIL import Image, ImageTk
import ctypes
ct=2
cvt=2
rt=2
def oi():
    global img1,realimg,rs
    w.img1=tkinter.filedialog.askopenfilename(filetypes=(("png files", "*.png"), ("jpg files", "*.jpg"), ("jpeg files", "*.jpeg")))
    realimg=Image.open(w.img1)
    rs=realimg.resize((1080,720))
    global tki
    tki=ImageTk.PhotoImage(rs)
    global yechap
    yechap=Label(img,image=tki).place(x=1,y=0)


def fi():
    global ct
    if ct%2==0:
    
        global rs
        rs=rs.transpose(Image.FLIP_LEFT_RIGHT)
        global hi
        hi=ImageTk.PhotoImage(rs)
        yechap=Label(img,image=hi).place(x=1,y=0)
        ct=ct+1
    else:
        hi=ImageTk.PhotoImage(rs)
        yechap=Label(img,image=hi).place(x=1,y=0)
        ct=2

def vi():
    global cvt
    if cvt%2==0:
        global rs
        rs=rs.transpose(Image.FLIP_TOP_BOTTOM)
        global hi
        hi=ImageTk.PhotoImage(rs)
        yechap=Label(img,image=hi).place(x=1,y=0)
        cvt=cvt+1
    else:
        hi=ImageTk.PhotoImage(rs)
        yechap=Label(img,image=hi).place(x=1,y=0)
        cvt=2

def rl():
    global rt
    if rt%2==0:
        global rs
        rs=rs.transpose(Image.FLIP_TOP_BOTTOM)
        global hi
        hi=ImageTk.PhotoImage(rs)
        yechap=Label(img,image=hi).place(x=1,y=0)
        rt=rt+1
    else:
        hi=ImageTk.PhotoImage(rs)
        yechap=Label(img,image=hi).place(x=1,y=0)
        rt=2
    
   
 
  

    

w=tkinter.Tk()
ctypes.windll.shcore.SetProcessDpiAwareness(2)



w.title("IMAGE EDITOR-WOC-4.0")
w.geometry('1940x1080')
w.configure(bg="#000000")

img=tkinter.Canvas(w, width=1080,height=720,bg="Grey")
img.grid(column=0,row=0,columnspan=10)

open=tkinter.Button(w,text='Open',width=5,padx=15,pady=10,bg="GREY",fg="White",font='Arial',command=oi)
open.grid(column=12,row=0,padx=5,pady=5,sticky="N")

save=tkinter.Button(w,text='Save',width=5,padx=15,pady=10,bg="GREY",fg="White",font='Arial')
save.grid(column=13,row=0,padx=10,pady=5,sticky="N")

Crop=tkinter.Button(w,text='Crop',width=5,padx=5,pady=10,bg="GREY",fg="White",font='Arial')
Crop.grid(column=0,row=2,padx=5,pady=5,sticky="W")

BW=tkinter.Button(w,text='Black and White',width=15,padx=5,pady=10,bg="GREY",fg="White",font='Arial')
BW.grid(column=1,row=2,padx=5,pady=5,sticky="W")

ic=tkinter.Button(w,text='Invert Colour',width=15,padx=5,pady=10,bg="GREY",fg="White",font='Arial')
ic.grid(column=2,row=2,padx=5,pady=5,sticky="W")


hf=tkinter.Button(w,text='Horizontal flip',width=15,padx=5,pady=10,bg="GREY",fg="White",font='Arial',command=fi)
hf.grid(column=3,row=2,padx=5,pady=5,sticky="W")

vf=tkinter.Button(w,text='Vertical flip',width=15,padx=5,pady=10,bg="GREY",fg="White",font='Arial',command=vi)
vf.grid(column=4,row=2,padx=5,pady=5,sticky="W")

rl=tkinter.Button(w,text='Rotate Left ⟳',width=15,padx=5,pady=10,bg="GREY",fg="White",font='Arial')
rl.grid(column=5,row=2,padx=5,pady=5,sticky="W")

rr=tkinter.Button(w,text='Rotate Right ⟳',width=15,padx=5,pady=10,bg="GREY",fg="White",font='Arial')
rr.grid(column=6,row=2,padx=5,pady=5,sticky="W")



w.mainloop()