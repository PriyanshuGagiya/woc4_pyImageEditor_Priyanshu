from cProfile import label
from tkinter import *
import tkinter
import tkinter.filedialog 
from tkinter.ttk import *
from PIL import Image, ImageTk,ImageChops,ImageOps,ImageEnhance
import ctypes

bc=2
ivcc=2
def oi():
    global img1,realimg,rs
    w.img1=tkinter.filedialog.askopenfilename(filetypes=( ("jpg files", "*.jpg"), ("png files", "*.png"),("jpeg files", "*.jpeg")))
    realimg=Image.open(w.img1)
    rs=realimg.resize((1080,720))
    global tki
    tki=ImageTk.PhotoImage(rs)
    global yechap
    yechap=Label(img,image=tki).place(x=1,y=0)



def fi():
   
        global rs
        rs=rs.transpose(Image.FLIP_LEFT_RIGHT)
        global hi
        hi=ImageTk.PhotoImage(rs)
        yechap=Label(img,image=hi).place(x=1,y=0)
    
 

def vi():
    
        global rs
        rs=rs.transpose(Image.FLIP_TOP_BOTTOM)
        global hi
        hi=ImageTk.PhotoImage(rs)
        yechap=Label(img,image=hi).place(x=1,y=0)
     

def rol():
        global rs
        rs=rs.transpose(Image.ROTATE_90)
        global hi
        rs=rs.resize((1080,720))
        hi=ImageTk.PhotoImage(rs)
        yechap=Label(img,image=hi).place(x=1,y=0)
      
def ror():
        global rs
        rs=rs.transpose(Image.ROTATE_270)
        global hi
        rs=rs.resize((1080,720))
        hi=ImageTk.PhotoImage(rs)
        yechap=Label(img,image=hi).place(x=1,y=0)

def bw():
        global bc
        if bc%2==0:
                bc=3
                global rs 
                global bcha
                bcha=rs
                bcha=bcha.convert("L")
                global hi
                hi=ImageTk.PhotoImage(bcha)
                yechap=Label(img,image=hi).place(x=1,y=0)
        else:
                hi=ImageTk.PhotoImage(rs)
                yechap=Label(img,image=hi).place(x=1,y=0)
                bc=2
def ivc():
        global rs
        pixels = rs.load()

        for i in range(rs.size[0]):
                for j in range(rs.size[1]):
                        x,y,z = pixels[i,j][0],pixels[i,j][1],pixels[i,j][2]
                        x,y,z = abs(x-255), abs(y-255), abs(z-255)
                        pixels[i,j] = (x,y,z)

        global hi
        hi=ImageTk.PhotoImage(rs)
        yechap=Label(img,image=hi).place(x=1,y=0)
    
def saves():
        global rs
        rs= rs.save("save1.jpg")
def crop():
        global rs
        rs = rs.crop((1,2,300,300))
        rs=rs.resize((1080,720))
        global hi
        hi=ImageTk.PhotoImage(rs)
        yechap=Label(img,image=hi).place(x=1,y=0)


def enh():
        global rs       
        global hi
        rs=ImageEnhance.Sharpness(rs)
        rs=rs.enhance(sharpness.get())
        hi=ImageTk.PhotoImage(rs)
        yechap=Label(img,image=hi).place(x=1,y=0)

def bri():
        global rs       
        global hi
        rs=ImageEnhance.Brightness(rs)
        rs=rs.enhance(b.get())
        hi=ImageTk.PhotoImage(rs)
        yechap=Label(img,image=hi).place(x=1,y=0)
w=tkinter.Tk()
ctypes.windll.shcore.SetProcessDpiAwareness(2)

sharpness=DoubleVar(w,value=1.0)
b=DoubleVar(w,value=1.0)

w.title("IMAGE EDITOR-WOC-4.0")
w.geometry('1940x1080')
w.configure(bg="#000000")

img=tkinter.Canvas(w, width=1080,height=720,bg="Grey")
img.grid(column=0,row=0,columnspan=10)

open=tkinter.Button(w,text='Open',width=5,padx=15,pady=10,bg="GREY",fg="White",font='Arial',command=oi)
open.grid(column=12,row=0,padx=5,pady=5,sticky="N")

save=tkinter.Button(w,text='Save',width=5,padx=15,pady=10,bg="GREY",fg="White",font='Arial',command=saves)
save.grid(column=13,row=0,padx=10,pady=5,sticky="N")

Crop=tkinter.Button(w,text='Crop',width=5,padx=5,pady=10,bg="GREY",fg="White",font='Arial',command=crop)
Crop.grid(column=0,row=2,padx=5,pady=5,sticky="W")

BW=tkinter.Button(w,text='Black and White',width=15,padx=5,pady=10,bg="GREY",fg="White",font='Arial',command=bw)
BW.grid(column=1,row=2,padx=5,pady=5,sticky="W")

ic=tkinter.Button(w,text='Invert Colour',width=15,padx=5,pady=10,bg="GREY",fg="White",font='Arial',command=ivc)
ic.grid(column=2,row=2,padx=5,pady=5,sticky="W")


hf=tkinter.Button(w,text='Horizontal flip',width=15,padx=5,pady=10,bg="GREY",fg="White",font='Arial',command=fi)
hf.grid(column=3,row=2,padx=5,pady=5,sticky="W")

vf=tkinter.Button(w,text='Vertical flip',width=15,padx=5,pady=10,bg="GREY",fg="White",font='Arial',command=vi)
vf.grid(column=4,row=2,padx=5,pady=5,sticky="W")

rl=tkinter.Button(w,text='Rotate Left ⟳',width=15,padx=5,pady=10,bg="GREY",fg="White",font='Arial',command=rol)
rl.grid(column=5,row=2,padx=5,pady=5,sticky="W")

rr=tkinter.Button(w,text='Rotate Right ⟳',width=15,padx=5,pady=10,bg="GREY",fg="White",font='Arial',command=ror)
rr.grid(column=6,row=2,padx=5,pady=5,sticky="W")

sharps = Scale(w, variable =sharpness, from_ = 0.08, to = 2.000000000, orient = HORIZONTAL)
sharps.grid(row = 3, column = 1, sticky = W, pady = 0, padx = 7, ipadx=5)

sharp = tkinter.Button(w, text='Set Sharpness', width=12, background="Grey", foreground="white", borderwidth=2, font="calibri",command=enh)
sharp.grid(row = 3, column = 2, sticky = W, pady = 0, padx = 7, ipadx=5)

brights = Scale(w, variable =b, from_ = 0.08, to = 2.000000, orient = HORIZONTAL)
brights.grid(row = 3, column = 3, sticky = W, pady = 0, padx = 7, ipadx=5)

bright = tkinter.Button(w, text='Set brightness', width=12, background="Grey", foreground="white", borderwidth=2, font="calibri",command=bri)
bright.grid(row = 3, column = 4, sticky = W, pady = 0, padx = 7, ipadx=5)

w.mainloop()
