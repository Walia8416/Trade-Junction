import tkinter as tk
import registration
import home
from tkinter import messagebox
import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='123456'
)
mycursor = mydb.cursor()

mycursor.execute('use tradejunction')


def login():

    if len(username.get()) == 0:
        tk.messagebox.showerror('Error', 'Please Enter Username!')

    elif len(password.get()) == 0:
        tk.messagebox.showerror('Error', 'Please Enter Password!')

    else:
        mycursor.execute("select * from Users where Username='" +
                         str(username.get())+"' AND Pass='"+str(password.get())+"'")
        c = 0
        for x in mycursor:
            c += 1
        if c == 0:
            tk.messagebox.showerror('Error', 'Invalid Password Or Username')

        else:
            tk.messagebox.showinfo(
                'Success', 'You have been logged in successfully!')
            
            win.destroy()
            home.homeScreen()


win = tk.Tk()
win.geometry('350x350')
win.resizable(False, False)
win.title('LOGIN')
ffg = 'black'

username = tk.StringVar()
password = tk.StringVar()

headLabel = tk.Label(win, text="Trade Junction")
headLabel.config(font=('Courier', 24, 'bold', 'underline'), fg=ffg)
headLabel.place(x=35, y=20)

userLabel = tk.Label(win, text="Username:")
userLabel.config(font=('Courier', 14, 'bold'), fg=ffg)
userLabel.place(x=35, y=150)
userEntry = tk.Entry(win, bd=2, textvariable=username)
userEntry.place(x=145, y=155)

passLabel = tk.Label(win, text="Password:")
passLabel.config(font=('Courier', 14, 'bold'), fg=ffg)
passLabel.place(x=35, y=200)
passEntry = tk.Entry(win, bd=2, textvariable=password, show="*")
passEntry.place(x=145, y=205)

login = tk.Button(win, text="Login", width=8, bd=2,
                  activeforeground='green', command=login, cursor='hand2')
login.config(font=('Arial, 12'))
login.place(x=250, y=300)

register = tk.Button(win, text="Register", width=8,
                     bd=2, command=registration.registerScreen, cursor='hand2')
register.config(font=('Arial, 12'))
register.place(x=20, y=300)

win.mainloop()
