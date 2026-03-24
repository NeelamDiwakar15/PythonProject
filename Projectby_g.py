from tkinter import*
from tkcalendar import Calendar,DateEntry
from tkinter import ttk
from PIL import ImageTk,Image
import datetime
from tkinter import messagebox


top=Tk()
top.geometry('1400x700')
top.title('Welcome')
top.resizable(0,0)
def UpdateForm():
    top2=Toplevel()
    top2.geometry('1400x700')
    top2.title('Update')
    top2.resizable(0,0)
    def Update():
        k=e1.get()
        k2=e2.get()
        k3=e3.get()
        k4=int(e4.get())
        format='%m/%d/%y'
        s=cal.get()
        date=datetime.datetime.strptime(s,format)
        n=date.strftime('%Y-%m-%d')
        k6=e5.get()
        k7=cb.get()
        k8=var.get() 
        import pymysql as sql
        db=sql.connect(host='localhost',user='root',password='123456',db='Regis_form')
        cur=db.cursor()
        s="update form set lastname=%s,password=%s,contact=%s,dob=%s,email=%s,city=%s,gender=%s where name=%s"
        g=(k2,k3,k4,n,k6,k7,k8,k)
        result=cur.execute(s,g)
        if result>0:
            messagebox.showinfo("Result","your record update successfully")
        else:
            messagebox.showinfo("Result","Data not found to update")
        db.commit()
        e1.delete(0,"end")
        e2.delete(0,"end")
        e3.delete(0,"end")
        e4.delete(0,"end")
        e5.delete(0,"end")
        cb.current(0)
    homeimg2=ImageTk.PhotoImage(file=r"C:\Users\diwak\Downloads\turt.jpg")
    L5=Label(top2,image=homeimg2)
    L5.pack()
    var=StringVar()
    
    
    k=['Select','Meerut','Delhi','Noida','Champaran','gurugram']
    L1=Label(top2,text='Updation_form',fg='Black',bg='Orange',font=('Arial 25 bold'))
    L1.place(x=500,y=10)

    L2=Label(top2,text='Name',fg='black',bg='Yellow',font=('Arial 20 bold'))
    L2.place(x=100,y=150)
    e1=Entry(top2,font=('Arial 18 italic'))
    e1.place(x=250,y=150)

    L3=Label(top2,text='LastName',fg='black',bg='Yellow',font=('Arial 20 bold'))
    L3.place(x=100,y=200)
    e2=Entry(top2,font=('Arial 18 italic'))
    e2.place(x=250,y=200)

    L4=Label(top2,text='Password',fg='black',bg='Yellow',font=('Arial 20 bold'))
    L4.place(x=100,y=250)
    e3=Entry(top2,font=('Arial 18 bold'),show="*")#show * to hide password
    e3.place(x=250,y=250)
    c1=Checkbutton(top2,font=('Arial 18 bold'),command=showpassword)
    c1.place(x=500,y=245)

    L5=Label(top2,text='Contact',fg='black',bg='Yellow',font=('Arial 20 bold'))
    L5.place(x=100,y=300)
    e4=Entry(top2,font=('Arial 18 bold'))
    e4.place(x=250,y=300)

    L6=Label(top2,text='DOB',fg='black',bg='Yellow',font=('Arial 20 bold'))
    L6.place(x=100,y=350)
    cal=DateEntry(top2,width=20,bg="Green",fg="white",year=2010)
    cal.place(x=250,y=350)

    L7=Label(top2,text='Email',fg='black',bg='Yellow',font=('Arial 20 bold'))
    L7.place(x=100,y=400)
    e5=Entry(top2,font=('Arial 18 bold'))
    e5.place(x=250,y=400)

    L8=Label(top2,text='City',fg='black',bg='Yellow',font=('Arial 20 bold'))
    L8.place(x=100,y=450)
    cb=ttk.Combobox(top2,value=k,font=('Arial 18 bold'))
    cb.place(x=250,y=450)
    cb.current(0)

    
    L9=Label(top2,text='Gender',fg='black',bg='Yellow',font=('Arial 18 bold'))
    L9.place(x=100,y=500)
    r1=Radiobutton(top2,variable=var,value='male',text='Male',font=('Arial 18 italic'))
    r1.place(x=250,y=500)
    r2=Radiobutton(top2,variable=var,value='female',text='Female',font=('Arial 18 italic'))
    r2.place(x=350,y=500)
    r3=Radiobutton(top2,variable=var,value='other',text='Other',font=('Arial 18 italic'))
    r3.place(x=470,y=500)

    b=Button(top2,text='Update',fg='white',bg='black',font=('Arial 25 bold'),command=Update)
    b.place(x=400,y=600)
    top2.config(bg='Blue')
    top2.mainloop()



def Login():
    top.destroy()
    import login_form

def Search():
    k=e1.get()
    for i in tv.get_children():
        tv.delete(i)
    import pymysql as sql
    db=sql.connect(host='localhost',user='root',password='123456',db='Regis_form')
    cur=db.cursor()
    p="select *from form where name=%s"
    cur.execute(p,k)
    result=cur.fetchall()
    for col in result:
        name=col[0]
        lastname=col[1]
        password=col[2]
        contact=col[3]
        dob=col[4]
        email=col[5]
        city=col[6]
        gender=col[7]
        tv.insert("",'end',values=(name,lastname,password,contact,dob,email,city,gender))
    

def showpassword():
    if e3.cget('show')=="*":
        e3.config(show='')
    else:
        e3.config(show="*")

def show():
    for i in tv.get_children():
        tv.delete(i)
        
    import pymysql as sql
    db=sql.connect(host='localhost',user='root',password='123456',db='Regis_form')
    cur=db.cursor()
    p="select *from form"
    cur.execute(p)
    result=cur.fetchall()
    for col in result:
        name=col[0]
        lastname=col[1]
        password=col[2]
        contact=col[3]
        dob=col[4]
        email=col[5]
        city=col[6]
        gender=col[7]
        tv.insert("",'end',values=(name,lastname,password,contact,dob,email,city,gender))
        ##print(name,lastname,password,contact,dob,email,city,gender)

def Delete():
    k=e1.get()
    import pymysql as sql
    db=sql.connect(host='localhost',user='root',password='123456',db='Regis_form')
    cur=db.cursor()
    s="delete from form where name=%s"
    result=cur.execute(s,k)
    if(result>0):
        messagebox.showinfo("Result","your record delete successfully")
    else:
        messagebox.showinfo("Result","your record not deleted")
    db.commit()
    
def Insert():
    k=e1.get()
    k2=e2.get()
    k3=e3.get()
    k4=int(e4.get())
    format='%m/%d/%y'
    s=cal.get()
    date=datetime.datetime.strptime(s,format)
    n=date.strftime('%Y-%m-%d')
    k6=e5.get()
    k7=cb.get()
    k8=var.get() 
    import pymysql as sql
    db=sql.connect(host='localhost',user='root',password='123456',db='Regis_form')
    cur=db.cursor()
    s="insert into form values('%s','%s','%s','%s','%s','%s','%s','%s')"%(k,k2,k3,k4,n,k6,k7,k8)
    result=cur.execute(s)
    if(result>0):
        messagebox.showinfo("Result","your record insert successfully")
    else:
        messagebox.showinfo("Result","your record not inserted")
    db.commit()
    e1.delete(0,"end")
    e2.delete(0,"end")
    e3.delete(0,"end")
    e4.delete(0,"end")
    e5.delete(0,"end")
    cb.current(0)
    
homeimg=ImageTk.PhotoImage(file=r"C:\Users\diwak\Downloads\cr.jpg")
L44=Label(top,image=homeimg)
L44.pack()


tv = ttk.Treeview(top,height=15)
tv['columns']=('name','lastname','password','contact','dob','email','city','gender')

tv.column('#0', width=0, stretch=NO)
tv.column('name', anchor=CENTER, width=100)
tv.column('lastname', anchor=CENTER, width=80)
tv.column('password', anchor=CENTER, width=100)
tv.column('contact', anchor=CENTER, width=95)
tv.column('dob', anchor=CENTER, width=100)
tv.column('email', anchor=CENTER, width=140)
tv.column('city', anchor=CENTER, width=100)
tv.column('gender', anchor=CENTER, width=60)


tv.heading('name', text='Name', anchor=CENTER)
tv.heading('lastname', text='Lastname', anchor=CENTER)
tv.heading('password', text='Password', anchor=CENTER)
tv.heading('contact', text='Contact', anchor=CENTER)
tv.heading('dob', text='Dob', anchor=CENTER)
tv.heading('email', text='Email', anchor=CENTER)
tv.heading('city', text='City', anchor=CENTER)
tv.heading('gender', text='Gender', anchor=CENTER)

tv.place(x=560,y=150)

k=['Select','Meerut','Delhi','Noida','Champaran','gurugram']
L1=Label(top,text='Registration',fg='Black',bg='Orange',font=('Arial 25 bold'))
L1.place(x=500,y=10)

L2=Label(top,text='Name',fg='black',bg='Yellow',font=('Arial 20 bold'))
L2.place(x=100,y=150)
e1=Entry(top,font=('Arial 18 italic'))
e1.place(x=250,y=150)

L3=Label(top,text='LastName',fg='black',bg='Yellow',font=('Arial 20 bold'))
L3.place(x=100,y=200)
e2=Entry(top,font=('Arial 18 italic'))
e2.place(x=250,y=200)

L4=Label(top,text='Password',fg='black',bg='Yellow',font=('Arial 20 bold'))
L4.place(x=100,y=250)
e3=Entry(top,font=('Arial 18 bold'),show="*")#show * to hide password
e3.place(x=250,y=250)
c1=Checkbutton(top,font=('Arial 18 bold'),command=showpassword)
c1.place(x=500,y=245)

L5=Label(top,text='Contact',fg='black',bg='Yellow',font=('Arial 20 bold'))
L5.place(x=100,y=300)
e4=Entry(top,font=('Arial 18 bold'))
e4.place(x=250,y=300)

L6=Label(top,text='DOB',fg='black',bg='Yellow',font=('Arial 20 bold'))
L6.place(x=100,y=350)
cal=DateEntry(top,width=20,bg="Green",fg="white",year=2010)
cal.place(x=250,y=350)

L7=Label(top,text='Email',fg='black',bg='Yellow',font=('Arial 20 bold'))
L7.place(x=100,y=400)
e5=Entry(top,font=('Arial 18 bold'))
e5.place(x=250,y=400)

L8=Label(top,text='City',fg='black',bg='Yellow',font=('Arial 20 bold'))
L8.place(x=100,y=450)
cb=ttk.Combobox(top,value=k,font=('Arial 18 bold'))
cb.place(x=250,y=450)
cb.current(0)

var=StringVar()
L9=Label(top,text='Gender',fg='black',bg='Yellow',font=('Arial 18 bold'))
L9.place(x=100,y=500)
r1=Radiobutton(top,variable=var,value='male',text='Male',font=('Arial 18 italic'))
r1.place(x=250,y=500)
r2=Radiobutton(top,variable=var,value='female',text='Female',font=('Arial 18 italic'))
r2.place(x=350,y=500)
r3=Radiobutton(top,variable=var,value='other',text='Other',font=('Arial 18 italic'))
r3.place(x=470,y=500)

b=Button(top,text='submit',fg='white',bg='black',font=('Arial 25 bold'),command=Insert)
b.place(x=400,y=600)
b1=Button(top,text='Delete',fg='white',bg='black',font=('Arial 25 bold'),command=Delete)
b1.place(x=550,y=600)
b2=Button(top,text='Show',fg='white',bg='black',font=('Arial 25 bold'),command=show)
b2.place(x=690,y=600)
b3=Button(top,text='Search',fg='white',bg='black',font=('Arial 25 bold'),command=Search)
b3.place(x=820,y=600)
b4=Button(top,text='Login',fg='white',bg='black',font=('Arial 25 bold'),command=Login)
b4.place(x=975,y=600)
b5=Button(top,text='Update',fg='white',bg='black',font=('Arial 25 bold'),command=UpdateForm)
b5.place(x=1105,y=600)  


top.config(bg='Blue')

top.mainloop()
