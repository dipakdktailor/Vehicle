from tkinter import *
import tkinter as tk
from tkinter import messagebox
from tkinter.ttk import *
from PIL import ImageTk, Image
import pymysql
db=pymysql.connect("localhost","root","","vechile")
cursor=db.cursor()

root = tk.Tk()
root.title("Regional Transport Office")
root.wm_state('zoomed')
img = Image.open("1.jpg")
rimg = img.resize((1366, 740))
photo = ImageTk.PhotoImage(rimg)
panel = Label(root, image = photo)
panel.pack()

lbl1 = Label(root, text="Welcome to Regional Transport Office",font=("arial", "30"))
lbl1.configure(bg = "#BAAFAD")
lbl1.place(x=350, y=10)

def admin():
    top = Toplevel()
    top.title = ("Admin Login")
    top.geometry("1366x768")

    lbl1 = Label(top, text="Welcome to Regional Transport Office",bg="red",font=("arial", "30"))
    lbl1.place(x=350, y=10)

    lbl = Label(top, text="Please Admin Login Here", font=("arial", "25"))
    lbl.place(x=500, y=100)

    lbl2 = Label(top, text="Login ID", font=("arial", 15))
    lbl2.place(x=400, y=200)
    txt1 = Entry(top, text="")
    txt1.place(x=550, y=200)
    txt1.config(width=50)

    lbl3 = Label(top, text="Password", font=("arial", 15))
    lbl3.place(x=400, y=300)
    txt2 = Entry(top, text="")
    txt2.place(x=550, y=300)
    txt2.config(width=50)

    def admin_submit():
        a = int(txt1.get())
        sql = "select id from admin"
        cursor.execute(sql)
        b = cursor.fetchone()
        c = txt2.get()
        txt2.delete(0, END)
        sql1 = "SELECT password from admin"
        cursor.execute(sql1)
        d = cursor.fetchone()
        if a == b[0]:
            if c == d[0]:
                messagebox.showinfo("Logged In", "Now You Are Logged In As Admin")
                top1 = Toplevel()
                top1.title = ("Add The Vechile Information")
                top1.geometry("1366x768")

                lbl81 = Label(top1, text="Welcome to Regional Transport Office", font=("arial", "30"))
                lbl81.place(x=350, y=10)

                lbl82 = Label(top1, text="Add The Vechile Information", font=("arial", "25"))
                lbl82.place(x=500, y=100)

                lbl83 = Label(top1, text="Owner's Name", font=("arial", 15))
                lbl83.place(x=400, y=200)
                txt81 = Entry(top1, text="")
                txt81.place(x=600, y=200)
                txt81.config(width=50)

                lbl84 = Label(top1, text="Father Name", font=("arial", 15))
                lbl84.place(x=400, y=250)
                txt82 = Entry(top1, text="")
                txt82.place(x=600, y=250)
                txt82.config(width=50)

                lbl85 = Label(top1, text="Mother Name", font=("arial", 15))
                lbl85.place(x=400, y=300)
                txt83 = Entry(top1, text="")
                txt83.place(x=600, y=300)
                txt83.config(width=50)

                lbl86 = Label(top1, text="Vechile Type", font=("arial", 15))
                lbl86.place(x=400, y=350)

                number81 = StringVar()
                cb81 = Combobox(top1, textvariable=number81, state="readonly")
                cb81['values'] = (
                "---------------------Vechile Type-----------------------", "Two Wheeler", "Three Wheeler",
                "Four Wheeler", "Large Vechile")
                cb81.place(x=600, y=350)
                cb81.current(0)
                cb81.config(width=47)

                lbl87 = Label(top1, text="Veichle Reg. No.", font=("arial", 15))
                lbl87.place(x=400, y=400)
                txt84 = Entry(top1, text="")
                txt84.place(x=600, y=400)
                txt84.config(width=50)

                lbl88 = Label(top1, text="Veichle Engine No.", font=("arial", 15))
                lbl88.place(x=400, y=450)
                txt85 = Entry(top1, text="")
                txt85.place(x=600, y=450)
                txt85.config(width=50)

                lbl89 = Label(top1, text="ID Proof", font=("arial", 15))
                lbl89.place(x=400, y=500)
                txt86 = Entry(top1, text="")
                txt86.place(x=600, y=500)
                txt86.config(width=50)

                lbl90 = Label(top1, text="ID Type", font=("arial", 15))
                lbl90.place(x=400, y=550)

                number82 = StringVar()
                cb82 = Combobox(top1, textvariable=number82, state="readonly")
                cb82['values'] = (
                    "---------------------ID Type-----------------------", "Aadhar Card", "PAN Card")
                cb82.place(x=600, y=550)
                cb82.current(0)
                cb82.config(width=47)

                def a_submit():
                    a=txt81.get()
                    b=txt82.get()
                    c=txt83.get()
                    d=number81.get()
                    e=txt84.get()
                    f=txt85.get()
                    g=txt86.get()
                    h = number82.get()
                    x = "INSERT into admin_info (name,fname,mname,vtype,regno,engineno,idproof,idtype)values('%s','%s','%s','%s','%s','%s','%s','%s')" % (
                    a, b, c, d, e, f,g,h)
                    cursor.execute(x)
                    db.commit()
                    txt81.delete(0,END)
                    txt82.delete(0,END)
                    txt83.delete(0,END)
                    txt84.delete(0,END)
                    txt85.delete(0,END)
                    txt86.delete(0,END)
                    messagebox.showinfo("Update Information", "Successfully Updated")

                btn81 = Button(top1, text="Submit",command=a_submit)
                btn81.place(x=800, y=600)

                btn82 = Button(top1, text="Click Here To Get The All User Information")
                btn82.place(x=100, y=650)
                btn82.config(width=200)

            else:
                messagebox.showerror("value", "password error")
        else:
            messagebox.showerror("value", "ID error")

    btn1 = Button(top, text="Submit",command=admin_submit)
    btn1.place(x=800, y=350)

def user():
    top = Toplevel()
    top.title = ("Admin Login")
    top.geometry("1366x768")

    lbl11 = Label(top, text="Welcome to Regional Transport Office",font=("arial", "30"))
    lbl11.place(x=350, y=10)

    lbl12 = Label(top, text="Search Your Veichle", font=("arial", "25"))
    lbl12.place(x=500, y=100)

    lbl13 = Label(top, text="Your Name", font=("arial", 15))
    lbl13.place(x=400, y=200)
    txt11 = Entry(top, text="")
    txt11.place(x=550, y=200)
    txt11.config(width=50)

    lbl14 = Label(top, text="Engine Number", font=("arial", 15))
    lbl14.place(x=400, y=250)
    txt12 = Entry(top, text="")
    txt12.place(x=550, y=250)
    txt12.config(width=50)

    lbl15 = Label(top, text="ID Proof", font=("arial", 15))
    lbl15.place(x=400, y=300)
    txt13 = Entry(top, text="")
    txt13.place(x=550, y=300)
    txt13.config(width=50)

    def user1():
        a=txt11.get()
        b=txt12.get()
        c=txt13.get()

        sql="select * from admin_info"
        cursor.execute(sql)
        d=cursor.fetchall()
        for i in d:
            if b==i[6]:
                for i in d:
                    if c==i[7]:
                        top2 = Toplevel()
                        top2.title = ("User Information")
                        top2.geometry("1366x768")

                        lbl21 = Label(top2, text="Welcome to Regional Transport Office", font=("arial", "30"))
                        lbl21.place(x=350, y=10)

                        lbl22 = Label(top2, text="Here Is The Information", font=("arial", "25"))
                        lbl22.place(x=500, y=70)

                        lbl91 = Label(top2,text="Your Name:-" ,font=("arial", 15))
                        lbl91.place(x=400, y=150)

                        lbl92 = Label(top2,text="Father Name:-", font=("arial", 15))
                        lbl92.place(x=400, y=200)

                        lbl93 = Label(top2,text="Mother Name:-", font=("arial", 15))
                        lbl93.place(x=400, y=250)

                        lbl94 = Label(top2,text="Vechile Type:-", font=("arial", 15))
                        lbl94.place(x=400, y=300)

                        lbl95 = Label(top2,text="Registration No.:-", font=("arial", 15))
                        lbl95.place(x=400, y=350)

                        lbl96 = Label(top2,text="Engine No.:-", font=("arial", 15))
                        lbl96.place(x=400, y=400)

                        lbl97 = Label(top2,text="ID Proof:-", font=("arial", 15))
                        lbl97.place(x=400, y=450)

                        lbl98 = Label(top2,text="ID Type:-", font=("arial", 15))
                        lbl98.place(x=400, y=500)

                        lbl101 = Label(top2, font=("arial", 15))
                        lbl101.place(x=700, y=150)

                        lbl102 = Label(top2, font=("arial", 15))
                        lbl102.place(x=700, y=200)

                        lbl103 = Label(top2,font=("arial", 15))
                        lbl103.place(x=700, y=250)

                        lbl104 = Label(top2, font=("arial", 15))
                        lbl104.place(x=700, y=300)

                        lbl105 = Label(top2, font=("arial", 15))
                        lbl105.place(x=700, y=350)

                        lbl106 = Label(top2, font=("arial", 15))
                        lbl106.place(x=700, y=400)

                        lbl107 = Label(top2, font=("arial", 15))
                        lbl107.place(x=700, y=450)

                        lbl108 = Label(top2, font=("arial", 15))
                        lbl108.place(x=700, y=500)

                        sql3 = "select * from admin_info where engineno='%s'"%(c)
                        cursor.execute(sql3)
                        d = cursor.fetchone()

                        lbl101.config(text=d[1])
                        lbl102.config(text=d[2])
                        lbl103.config(text=d[3])
                        lbl104.config(text=d[4])
                        lbl105.config(text=d[5])
                        lbl106.config(text=d[6])
                        lbl107.config(text=d[7])
                        lbl108.config(text=d[8])


    btn11 = Button(top, text="Search Your Vechile",command=user1)
    btn11.place(x=800, y=350)

def agencies():
    top = Toplevel()
    top.title = ("Admin Login")
    top.geometry("1366x768")

    lbl21 = Label(top, text="Welcome to Regional Transport Office",font=("arial", "30"))
    lbl21.place(x=350, y=10)

    lbl22 = Label(top, text="Please Agencies Login Here", font=("arial", "25"))
    lbl22.place(x=500, y=100)

    lbl23 = Label(top, text="Login ID", font=("arial", 15))
    lbl23.place(x=400, y=200)
    txt21 = Entry(top, text="")
    txt21.place(x=550, y=200)
    txt21.config(width=50)

    lbl24 = Label(top, text="Password", font=("arial", 15))
    lbl24.place(x=400, y=300)
    txt22 = Entry(top, text="")
    txt22.place(x=550, y=300)
    txt22.config(width=50)

    def agn():
        a = int(txt21.get())
        b = txt22.get()

        sql = "select * from agencies"
        cursor.execute(sql)
        d = cursor.fetchall()
        for i in d:
            if a == i[0]:
                for i in d:
                    if b == i[1]:
                        top2 = Toplevel()
                        top2.title = ("Agencies Here You Can Add Information")
                        top2.geometry("1366x768")

                        lbl21 = Label(top2, text="Welcome to Regional Transport Office", font=("arial", "30"))
                        lbl21.place(x=350, y=10)

                        lbl22 = Label(top2, text="Please Add The Information", font=("arial", "25"))
                        lbl22.place(x=500, y=100)

                        lbl33 = Label(top2, text="Your Name", font=("arial", 15))
                        lbl33.place(x=400, y=150)
                        txt31 = Entry(top2, text="")
                        txt31.place(x=600, y=150)
                        txt31.config(width=50)

                        lbl34 = Label(top2, text="Father Name", font=("arial", 15))
                        lbl34.place(x=400, y=200)
                        txt32 = Entry(top2, text="")
                        txt32.place(x=600, y=200)
                        txt32.config(width=50)

                        lbl35 = Label(top2, text="Mother Name", font=("arial", 15))
                        lbl35.place(x=400, y=250)
                        txt33 = Entry(top2, text="")
                        txt33.place(x=600, y=250)
                        txt33.config(width=50)

                        lbl36 = Label(top2, text="Vechile Type", font=("arial", 15))
                        lbl36.place(x=400, y=300)

                        number = StringVar()
                        cb = Combobox(top2, textvariable=number, state="readonly")
                        cb['values'] = (
                        "---------------------Vechile Type-----------------------", "Two Wheeler", "Three Wheeler",
                        "Four Wheeler", "Large Vechile")
                        cb.place(x=600, y=300)
                        cb.current(0)
                        cb.config(width=47)

                        lbl37 = Label(top2, text="Veichle Reg. No.", font=("arial", 15))
                        lbl37.place(x=400, y=350)
                        txt34 = Entry(top2, text="")
                        txt34.place(x=600, y=350)
                        txt34.config(width=50)

                        lbl38 = Label(top2, text="Veichle Engine No.", font=("arial", 15))
                        lbl38.place(x=400, y=400)
                        txt35 = Entry(top2, text="")
                        txt35.place(x=600, y=400)
                        txt35.config(width=50)

                        lbl39 = Label(top2, text="ID Proof(Any)", font=("arial", 15))
                        lbl39.place(x=400, y=450)
                        txt36 = Entry(top2, text="")
                        txt36.place(x=600, y=450)
                        txt36.config(width=50)

                        lbl40 = Label(top2, text="ID Type", font=("arial", 15))
                        lbl40.place(x=400, y=500)

                        number1 = StringVar()
                        cb1 = Combobox(top2, textvariable=number1, state="readonly")
                        cb1['values'] = (
                            "---------------------ID Type-----------------------", "Aadhar Card", "PAN Card")
                        cb1.place(x=600, y=500)
                        cb1.current(0)
                        cb1.config(width=47)

                        lbl41 = Label(top2, text="Agencey Name", font=("arial", 15))
                        lbl41.place(x=400, y=550)
                        txt37 = Entry(top2, text="")
                        txt37.place(x=600, y=550)
                        txt37.config(width=50)

                        lbl42 = Label(top2, text="Agencey Code", font=("arial", 15))
                        lbl42.place(x=400, y=600)
                        txt38 = Entry(top2, text="")
                        txt38.place(x=600, y=600)
                        txt38.config(width=50)

                        def a_info():
                            a=txt31.get()
                            b = txt32.get()
                            c = txt33.get()
                            d = txt34.get()
                            e = txt35.get()
                            f = txt36.get()
                            g = txt37.get()
                            h = txt38.get()
                            i=number.get()
                            j=number1.get()

                            x = "INSERT into agencies_info (name,fname,mname,vtype,regno,engineno,idproof,idtype,aname,acode)values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (
                                a, b, c,i, d, e, f,j, g, h)
                            cursor.execute(x)
                            db.commit()
                            txt31.delete(0, END)
                            txt32.delete(0, END)
                            txt33.delete(0, END)
                            txt34.delete(0, END)
                            txt35.delete(0, END)
                            txt36.delete(0, END)
                            txt37.delete(0, END)
                            txt38.delete(0, END)
                            messagebox.showinfo("Update Information", "Successfully Updated")

                        btn41 = Button(top2, text="Submit",command=a_info)
                        btn41.place(x=800, y=650)

    btn21 = Button(top, text="Submit",command=agn)
    btn21.place(x=800, y=350)

def form():
    top = Toplevel()
    top.title = ("Admin Login")
    top.geometry("1366x768")

    lbl31 = Label(top, text="Welcome to Regional Transport Office",font=("arial", "30"))
    lbl31.place(x=350, y=10)

    lbl32 = Label(top, text="Please Fill The Form", font=("arial", "25"))
    lbl32.place(x=500, y=100)

    lbl33 = Label(top, text="Your Name", font=("arial", 15))
    lbl33.place(x=400, y=200)
    txt31 = Entry(top, text="")
    txt31.place(x=600, y=200)
    txt31.config(width=50)

    lbl34 = Label(top, text="Father Name", font=("arial", 15))
    lbl34.place(x=400, y=250)
    txt32 = Entry(top, text="")
    txt32.place(x=600, y=250)
    txt32.config(width=50)

    lbl35 = Label(top, text="Mother Name", font=("arial", 15))
    lbl35.place(x=400, y=300)
    txt33 = Entry(top, text="")
    txt33.place(x=600, y=300)
    txt33.config(width=50)

    lbl36 = Label(top, text="Vechile Type", font=("arial", 15))
    lbl36.place(x=400, y=350)

    number=StringVar()
    cb=Combobox(top,textvariable=number,state="readonly")
    cb['values']=("---------------------Vechile Type-----------------------","Two Wheeler","Three Wheeler","Four Wheeler","Large Vechile")
    cb.place(x=600,y=350)
    cb.current(0)
    cb.config(width=47)

    lbl37 = Label(top, text="Veichle Reg. No.", font=("arial", 15))
    lbl37.place(x=400, y=400)
    txt34 = Entry(top, text="")
    txt34.place(x=600, y=400)
    txt34.config(width=50)

    lbl38 = Label(top, text="Veichle Engine No.", font=("arial", 15))
    lbl38.place(x=400, y=450)
    txt35 = Entry(top, text="")
    txt35.place(x=600, y=450)
    txt35.config(width=50)

    lbl39 = Label(top, text="ID Proof(Any)", font=("arial", 15))
    lbl39.place(x=400, y=500)
    txt36 = Entry(top, text="")
    txt36.place(x=600, y=500)
    txt36.config(width=50)

    lbl40 = Label(top, text="ID Type", font=("arial", 15))
    lbl40.place(x=400, y=550)

    number1 = StringVar()
    cb1 = Combobox(top, textvariable=number1, state="readonly")
    cb1['values'] = (
    "---------------------ID Type-----------------------", "Aadhar Card", "PAN Card")
    cb1.place(x=600, y=550)
    cb1.current(0)
    cb1.config(width=47)

    def form_user():
        a = txt31.get()
        b = txt32.get()
        c = txt33.get()
        d = txt34.get()
        e = txt35.get()
        f = txt36.get()
        i = number.get()
        j = number1.get()

        x = "INSERT into form (name,fname,mname,vtype,regno,engineno,idproof,idtype)values('%s','%s','%s','%s','%s','%s','%s','%s')" % (
            a, b, c, i, d, e, f, j,)
        cursor.execute(x)
        db.commit()
        txt31.delete(0, END)
        txt32.delete(0, END)
        txt33.delete(0, END)
        txt34.delete(0, END)
        txt35.delete(0, END)
        txt36.delete(0, END)
        messagebox.showinfo("Update Information", "Successfully Updated")


    btn31 = Button(top, text="Submit",command=form_user)
    btn31.place(x=800, y=600)

def rto():
    top = Toplevel()
    top.title = ("Admin Login")
    top.geometry("1366x768")

    lbl41 = Label(top, text="Welcome to Regional Transport Office",font=("arial", "30"))
    lbl41.place(x=350, y=10)

    lbl42 = Label(top, text="The Regional Transport Office or Regional Transport Authority (RTO/RTA) is the ", font=("arial", "15"))
    lbl42.place(x=400, y=100)
    lbl43=Label(top, text="organisation of the Indian government responsible for maintaining a database of drivers and a", font=("arial", "15"))
    lbl43.place(x=400, y=130)
    lbl44 = Label(top, text="database of vehicles for various states of India. The RTO issues driving licences, organises", font=("arial", "15"))
    lbl44.place(x=400, y=160)
    lbl45 = Label(top, text="collection of vehicle excise duty (also known as road tax and road fund licence) and sells", font=("arial", "15"))
    lbl45.place(x=400, y=190)
    lbl46 = Label(top, text="personalised registrations Along with this, the RTO is also responsible to inspect vehicle's", font=("arial", "15"))
    lbl46.place(x=400, y=220)
    lbl47 = Label(top, text="insurance and clear the pollution.", font=("arial", "15"))
    lbl47.place(x=400, y=250)

    lbl58 = Label(top, text="The owner of a vehicle can apply and get duplicate copy of the vehicle registration certificate  ",font=("arial", "15"))
    lbl58.place(x=400, y=350)
    lbl59 = Label(top,text="from the concerned RTO office if it is stolen, lost, destructed and completely written off. ",font=("arial", "15"))
    lbl59.place(x=400, y=380)
    lbl60 = Label(top,text="A complaint should be lodged to the police station which is situated under the jurisdiction / area ",font=("arial", "15"))
    lbl60.place(x=400, y=410)
    lbl61 = Label(top,text="of lost before approaching the regional transport officer. After completing the formalities, ",font=("arial", "15"))
    lbl61.place(x=400, y=440)
    lbl62 = Label(top,text="the owner has to submit FORM 26 and the Police Certificate to the Registering Authority along with the",font=("arial", "15"))
    lbl62.place(x=400, y=470)
    lbl63 = Label(top, text="equired documents for applying duplicate vehicle registration certificate.", font=("arial", "15"))
    lbl63.place(x=400, y=500)

def info():
    top = Toplevel()
    top.title = ("Admin Login")
    top.geometry("1366x768")

    lbl64 = Label(top, text="Welcome to Regional Transport Office", font=("arial", "30"))
    lbl64.place(x=350, y=10)

    lbl65 = Label(top, text="About Administration ",font=("arial", "25"))
    lbl65.place(x=500, y=100)
    lbl66 = Label(top,text="Nitin Jairam Gadkari About this sound pronunciation (born 27 May 1957) is ",font=("arial", "15"))
    lbl66.place(x=400, y=180)
    lbl67 = Label(top, text="an Indian politician and the current Minister for Road Transport & Highways,", font=("arial", "15"))
    lbl67.place(x=400, y=210)
    lbl68 = Label(top, text="in the Government of India.[1] Gadkari earlier served as the President of the ", font=("arial", "15"))
    lbl68.place(x=400, y=240)
    lbl69 = Label(top, text=" Bharatiya Janata Party from 2010-2013.[2] He is also known for the works during his ", font=("arial", "15"))
    lbl69.place(x=400, y=270)
    lbl70 = Label(top, text="tenure as a Public Works Department Minister in the state of Maharashtra when ", font=("arial", "15"))
    lbl70.place(x=400, y=300)
    lbl71 = Label(top, text="he constructed a series of roads, highways and flyovers across the state ", font=("arial", "15"))
    lbl71.place(x=400, y=330)

def contact():
    top = Toplevel()
    top.title = ("Admin Login")
    top.geometry("1366x768")

    lbl72 = Label(top, text="Welcome to Regional Transport Office", font=("arial", "30"))
    lbl72.place(x=350, y=10)

    lbl73 = Label(top, text="Contact Us ", font=("arial", "25"))
    lbl73.place(x=500, y=100)
    lbl74 = Label(top, text="Address    :- xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",font=("arial", "15"))
    lbl74.place(x=400, y=180)
    lbl75 = Label(top, text="Contact Us:-123xxxxxxx09",font=("arial", "15"))
    lbl75.place(x=400, y=210)
    lbl76 = Label(top, text=":-12xxxxxxxxxxxx5 ",font=("arial", "15"))
    lbl76.place(x=500, y=240)
    lbl77 = Label(top, text="PinCode    :- 3xxxx3",font=("arial", "15"))
    lbl77.place(x=400, y=270)
    lbl78 = Label(top, text="Fax No      :- xxxxxx",font=("arial", "15"))
    lbl78.place(x=400, y=300)
    lbl79 = Label(top, text="Email        :- abcdef@abc.com",font=("arial", "15"))
    lbl79.place(x=400, y=330)
    lbl80 = Label(top, text="Website    :- www.abc.com", font=("arial", "15"))
    lbl80.place(x=400, y=360)


mb = Menu(root)
fm = Menu(mb, tearoff = 0)
fm.add_command(label = "Admin Login",command=admin)
mb.add_cascade(label = "Admininstration", menu = fm)
fm = Menu(mb, tearoff = 0)
fm.add_command(label = "For User",command=user)
mb.add_cascade(label = "User", menu = fm)
fm = Menu(mb, tearoff = 0)
fm.add_command(label = "Agencies Login",command=agencies)
mb.add_cascade(label = "Agencies", menu = fm)
fm = Menu(mb, tearoff = 0)
fm.add_command(label = "New Form Submition",command=form)
mb.add_cascade(label = "Form Filling", menu = fm)
fm = Menu(mb, tearoff = 0)
fm.add_command(label = "About RTO",command=rto)
fm.add_command(label = "About Adminstration",command=info)
mb.add_cascade(label = "About Us", menu = fm)
fm = Menu(mb, tearoff = 0)
fm.add_command(label = "Our Contact Information",command=contact)
mb.add_cascade(label = "Contact Us", menu = fm)
root.configure(menu = mb)


root.mainloop()