from tkinter import *
from tkinter import messagebox
from matplotlib.style import use
import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='123456'
)
mycursor = mydb.cursor()
mycursor.execute('use tradejunction')

global fname, lname, age, username, password, addr, email, mob, AGpass


def registerScreen():
    global Rfname,Rlname,Rmob,Ruser,Raddr,Rpass,RpassAgain,Rage,Remail,ws
    ws = Tk()
    ws.resizable(False, False)
    ws.title('Registration')
    f = ('Times', 14)

    right_frame = Frame(
        ws,
        bd=2,
        bg='#CCCCCC',
        relief=SOLID,
        padx=12,
        pady=12
    )

    Label(
        right_frame,
        text="Enter First Name",
        bg='#CCCCCC',
        font=f
    ).grid(row=0, column=0, sticky=W, pady=10)

    Label(
        right_frame,
        text="Enter Last Name",
        bg='#CCCCCC',
        font=f
    ).grid(row=1, column=0, sticky=W, pady=10)

    Label(
        right_frame,
        text="Enter Email",
        bg='#CCCCCC',
        font=f
    ).grid(row=2, column=0, sticky=W, pady=10)

    Label(
        right_frame,
        text="Contact Number",
        bg='#CCCCCC',
        font=f
    ).grid(row=3, column=0, sticky=W, pady=10)

    Label(
        right_frame,
        text="Username",
        bg='#CCCCCC',
        font=f
    ).grid(row=4, column=0, sticky=W, pady=10)

    Label(
        right_frame,
        text="Enter Password",
        bg='#CCCCCC',
        font=f
    ).grid(row=5, column=0, sticky=W, pady=10)

    Label(
        right_frame,
        text="Re-Enter Password",
        bg='#CCCCCC',
        font=f
    ).grid(row=6, column=0, sticky=W, pady=10)

    Label(
        right_frame,
        text="Address",
        bg='#CCCCCC',
        font=f
    ).grid(row=7, column=0, sticky=W, pady=10)

    Label(
        right_frame,
        text="Age",
        bg='#CCCCCC',
        font=f
    ).grid(row=8, column=0, sticky=W, pady=10)

    Rfname = Entry(
        right_frame,
        font=f,
    )
    Rlname = Entry(
        right_frame,
        font=f,
    )

    Remail = Entry(
        right_frame,
        font=f,
    )
    Rmob = Entry(
        right_frame,
        font=f,
    )

    Ruser = Entry(
        right_frame,
        font=f,
    )
    Rpass = Entry(
        right_frame,
        font=f,
    )
    RpassAgain = Entry(
        right_frame,
        font=f,
    )
    Raddr = Entry(
        right_frame,
        font=f,
    )

    Rage = Entry(
        right_frame,
        font=f,
    )

    register_btn = Button(
        right_frame,
        width=15,
        text='Register',
        font=f,
        relief=SOLID,
        cursor='hand2',
        command=register
    )

    Rfname.grid(row=0, column=1, pady=10, padx=20)
    Rlname.grid(row=1, column=1, pady=10, padx=20)
    Remail.grid(row=2, column=1, pady=10, padx=20)

    Rmob.grid(row=3, column=1, pady=10, padx=20)
    Ruser.grid(row=4, column=1, pady=10, padx=20)
    Rpass.grid(row=5, column=1, pady=10, padx=20)
    RpassAgain.grid(row=6, column=1, pady=10, padx=20)
    Raddr.grid(row=7, column=1, pady=10, padx=20)
    Rage.grid(row=8, column=1, pady=10, padx=20)
    register_btn.grid(row=9, column=1, pady=10, padx=20)
    right_frame.pack()

    ws.mainloop()
# registration functions


def register():
    if len(Rfname.get()) == 0:
        messagebox.showerror('Error', 'Please Enter First Name!')

    elif len(Rlname.get()) == 0:
        messagebox.showerror('Error', 'Please Enter Last Name!')

    elif len(Rage.get()) == 0:
        messagebox.showerror('Error', 'Please Enter Age!')

    elif len(Ruser.get()) == 0:
        messagebox.showerror('Error', 'Please Enter Username!')

    elif len(Rpass.get()) == 0:
        messagebox.showerror('Error', 'Please Enter Password!')

    elif len(RpassAgain.get()) == 0:
        messagebox.showerror('Error', 'Please Enter Password!')

    elif len(Raddr.get()) == 0:
        messagebox.showerror('Error', 'Please Enter Address!')

    elif len(Remail.get()) == 0:
        messagebox.showerror('Error', 'Please Enter Email!')

    elif len(Rmob.get()) == 0:
        messagebox.showerror('Error', 'Please Enter Mobile No.!')

    elif Rpass.get() != RpassAgain.get():
        messagebox.showerror('Error', 'Passwords Do Not Match')

    else:
        print('sdf')
        mycursor.execute("insert into Users (FirstName,LastName,Age,Username,Pass,UserAddr,UserEmail,UserMob) values('"+Rfname.get()+"','"+Rlname.get()+"',"+Rage.get() +
                         ",'"+Ruser.get()+"','"+Rpass.get()+"','"+Raddr.get()+"','"+Remail.get()+"',"+Rmob.get()+")")
        
        mydb.commit()
        messagebox.showinfo(
                'Success', 'You have been registered successfully!')
        ws.destroy()
