from tkinter import*

from tkinter import ttk
from PIL import ImageTk,Image

from tkinter import messagebox


top=Tk()
top.geometry('1000x800')
top.title('Welcome')
top.resizable(0,0)

def LoginFetch():
    import pymysql as sql
    db=sql.connect(host='localhost',user='root',password='123456',db='Regis_form')
    cur=db.cursor()
    cur.execute("select *from form where name=%s and password=%s",(e1.get(),e2.get()))
    row=cur.fetchone()

    if row==None:
        messagebox.showerror("Error","Invalid username and password")
    else:
        top.destroy()
        import Projectby_g

def showpassword():
    if e2.cget('show')=="*":
        e2.config(show='')
    else:
        e2.config(show="*")

homeimg=ImageTk.PhotoImage(file=r"C:\Users\diwak\Downloads\3d.jpg")
L44=Label(top,image=homeimg)
L44.pack()

L1=Label(top,text='Login',fg='Black',bg='Orange',font=('Arial 25 bold'))
L1.place(x=500,y=10)

L2=Label(top,text='Name',fg='black',bg='Yellow',font=('Arial 20 bold'))
L2.place(x=100,y=150)
e1=Entry(top,font=('Arial 18 italic'))
e1.place(x=250,y=150)
L3=Label(top,text='Password',fg='black',bg='Yellow',font=('Arial 20 bold'))
L3.place(x=100,y=200)
e2=Entry(top,font=('Arial 18 bold'),show="*")
e2.place(x=250,y=200)
c1=Checkbutton(top,font=('Arial 18 bold'),command=showpassword)
c1.place(x=510,y=195)


b4=Button(top,text='Login',font=('Arial 18 italic'),command=LoginFetch)
b4.place(x=350,y=300)
top.mainloop()
