from tkinter import *
import matplotlib.pyplot as plt
import numpy as np

def kontrol():
    a=entA.get()
    if a=="" or a.replace(".","",1).replace("-","",1).isdigit()==False:
        entA.configure(bg="Red")
        au=False
    else:
        entA.configure(bg="Gray")
        au=True
    b=entB.get()
    if b=="" or b.replace(".","",1).replace("-","",1).isdigit()==False:
        entB.configure(bg="Red")
        bu=False
    else:
        entB.configure(bg="Gray")
        bu=True
    c=entC.get()
    if c=="" or c.replace(".","",1).replace("-","",1).isdigit()==False:
        entC.configure(bg="Red")
        cu=False
    else:
        entC.configure(bg="Gray")
        cu=True
    if au==True and bu==True and cu==True:
        u=True
        return u,a,b,c

def urav(event):
    u,a,b,c=kontrol()
    if u==True:
        b=float(b);c=float(c);a=float(a)
        D=(b**2)-(4*a*c)
        if D<0:
            lblRes.configure(text="D<0")
        else:
            x1=(-b-(D**(1/2)))/(2*a)
            x2=(-b+(D**(1/2)))/(2*a)
            x=f"D={D}\nx1={x1}\nx2={x2}"
            lblRes.configure(text=x)
            btnGraf=Button(win,text="Graafika",fg="Black",bg="Blue",font="Arial 20")
            btnGraf.pack(side=RIGHT)
            btnGraf.bind("<Button-1>",graf)

def graf(event):
    u,a,b,c=kontrol()
    b=float(b);c=float(c);a=float(a)
    D=(b**2)-(4*a*c)
    x1=(-b-(D**(1/2)))/(2*a)
    x2=(-b+(D**(1/2)))/(2*a)
    x=list(np.arange(x1,x2))
    y=[]
    for i in np.arange(x1,x2):
        y.append(float((i+0.5)**2 - 56.25))
    plt.title("Ruutvõrrand")
    plt.xlabel("x") 
    plt.ylabel("y") 
    plt.grid()      
    plt.plot(x,y) 
    plt.show()

win=Tk()
win.geometry("1200x600")
win.title("Math")

lbl=Label(win,text="Ruutvõrrandi lahendamine",fg="Black",font="Arial 30")
entA=Entry(win,fg="Black",justify=CENTER,bg="Grey",font="Arial 40",width=5)
lblx2=Label(win,text=" x**2 + ",fg="Black",font="Arial 40")
entB=Entry(win,fg="Black",justify=CENTER,bg="Grey",font="Arial 40",width=5)
lblx=Label(win,text=" x + ",fg="Black",font="Arial 40")
entC=Entry(win,fg="Black",justify=CENTER,bg="Grey",font="Arial 40",width=5)
lblk=Label(win,text=" = 0 ",fg="Black",font="Arial 40")
btnRes=Button(win,text="Otsustama",fg="Black",bg="Green",font="Arial 20")
lblRes=Label(win,text="Lahendus",fg="Black",bg="Grey",font="Arial 20",height=4)

lblRes.pack(side=BOTTOM, fill=X)
lbl.pack()
entA.pack(side=LEFT)
lblx2.pack(side=LEFT)
entB.pack(side=LEFT)
lblx.pack(side=LEFT)
entC.pack(side=LEFT)
lblk.pack(side=LEFT)
btnRes.pack(side=RIGHT)

btnRes.bind("<Button-1>",urav)


win.mainloop()
