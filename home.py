import mysql.connector
from functools import partial
from urllib.parse import uses_fragment
from ttkwidgets import Table
import tkinter as tk
from tkinter import ttk
import requests
from datetime import date


from stockInfo import stockInfo

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='123456'
)
mycursor = mydb.cursor()

mycursor.execute('use tradejunction')

f = open('stocks.txt', 'r')
ff = ('Times', 12)


def gen():

    if len(sym.get()) == 0:
        tk.messagebox.showerror('Error', 'Please Enter Symbol!')

    else:
        stockInfo(frame2, var.get(), sym.get())
        return None


def buy():
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={Bsym.get()}&apikey=Y4OVHTX2WGRVU8H6"
    r = requests.get(url)
    print(Bsym.get())
    print(vols.get())
    data = r.json()

    a = data["Time Series (Daily)"]
    c = 0
    stockVal = []
    for date in a:
        for value in a[date]:

            stockVal.append(a[date][value])

        c += 1
        if c > 0:
            break

    price = stockVal[0]

    mycursor.execute("insert into Buy (UserName,Symbol,Volume,AtPrice,BuyDate) values('" +
                     str(u[0][4])+"','"+str(Bsym.get())+"',"+str(vols.get()) + ","+str(price)+",now())")

    mydb.commit()


def homeScreen(user):
    global sym, var, u, root, frame2, vols, Bsym
    u = user
    root = tk.Tk()
    root.geometry('1000x500')
    root.title('Trade Junction')
    root.resizable(False, False)
    headLabel = tk.Label(root, text="Trade Junction")
    headLabel.config(font=('Courier', 29, 'bold', 'underline'), fg='black')
    headLabel.place(x=350, y=20)

    nameLabel = tk.Label(root, text=f"Welcome {user[0][1]} {user[0][2]}!")
    nameLabel.config(font=('Courier', 13), fg='black')
    nameLabel.place(x=10, y=20)

    notebook = ttk.Notebook(root)
    notebook.pack(pady=10, expand=True)
    frame1 = ttk.Frame(notebook, width=1000, height=180)
    frame2 = ttk.Frame(notebook, width=1000, height=180)
    frame3 = ttk.Frame(notebook, width=1000, height=180)
    frame4 = ttk.Frame(notebook, width=1000, height=180)
    frame5 = ttk.Frame(notebook, width=1000, height=180)
    frame1.pack(fill='both', expand=True)
    frame2.pack(fill='both', expand=True)
    frame3.pack(fill='both', expand=True)
    frame4.pack(fill='both', expand=True)
    frame5.pack(fill='both', expand=True)
    notebook.add(frame1, text='Real-Time Stock')
    notebook.add(frame2, text='Stock Info')
    notebook.add(frame3, text='Buy')
    notebook.add(frame4, text='My Portfolio')
    notebook.add(frame5, text='Profile')

    # REAL_TIME_STOCK INFO
    favLabel = tk.Label(frame1, text="WatchList")
    favLabel.config(font=('Courier', 12, 'bold', 'underline'), fg='black')
    favLabel.place(x=0, y=0)
    Dtable = ttk.Treeview(frame1, selectmode='browse')
    Dtable.place(x=0, y=30)
    verscrlbar = ttk.Scrollbar(frame1, orient='vertical', command=Dtable.yview)
    verscrlbar.place(x=970, y=0, height=180)
    Dtable.configure(xscrollcommand=verscrlbar.set)
    Dtable["columns"] = ("1", "2", "3", "4", "5", "6")
    Dtable['show'] = 'headings'

    Dtable.column("1", width=135, anchor='c')
    Dtable.column("2", width=166, anchor='c')
    Dtable.column("3", width=166, anchor='c')
    Dtable.column("4", width=166, anchor='c')
    Dtable.column("5", width=166, anchor='c')
    Dtable.column("6", width=166, anchor='c')
    Dtable.heading("1", text="Symbol")
    Dtable.heading("2", text="Open")
    Dtable.heading("3", text="High")
    Dtable.heading("4", text="Low")
    Dtable.heading("5", text="Close")
    Dtable.heading("6", text="Volume")

    for x in f:
        b = x.split()
        for stock in b:
            url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={stock}&apikey=Y4OVHTX2WGRVU8H6"
            r = requests.get(url)
            data = r.json()
            a = data["Time Series (Daily)"]
            c = 0
            stockVal = []
            for date in a:
                for value in a[date]:

                    stockVal.append(a[date][value])

                c += 1
                if c > 0:
                    break
            Dtable.insert("", 'end', text="L1", values=(
                stock, stockVal[0], stockVal[1], stockVal[2], stockVal[3], stockVal[4]))

    sym = tk.StringVar()
    Bsym = tk.StringVar()
    vols = tk.IntVar()
    # STOCK INFO
    stockLabel = tk.Label(frame2, text="Get Information On Any Stock")
    stockLabel.config(font=('Courier', 15, 'bold', 'underline'), fg='black')
    stockLabel.place(x=350, y=0)

    symbolLabel = tk.Label(frame2, text="Symbol:")
    symbolLabel.config(font=('Courier', 14, 'bold'), fg='black')
    symbolLabel.place(x=370, y=30)
    symbolEntry = tk.Entry(frame2, bd=2, textvariable=sym, width=10)
    symbolEntry.place(x=450, y=35)

    var = tk.IntVar()

    R1 = tk.Radiobutton(frame2, text="Company Overview", variable=var, value=1)
    R1.config(font=('Arial', 10))

    R2 = tk.Radiobutton(frame2, text="Income Statement", variable=var, value=2)
    R2.config(font=('Arial', 10))

    R3 = tk.Radiobutton(frame2, text="Balance Sheet", variable=var, value=3)
    R3.config(font=('Arial', 10))

    R4 = tk.Radiobutton(frame2, text="Cash Flow", variable=var, value=4)
    R4.config(font=('Arial', 10))

    R5 = tk.Radiobutton(frame2, text="Quarterly Earnings",
                        variable=var, value=5)
    R5.config(font=('Arial', 10))

    R6 = tk.Radiobutton(frame2, text="Price Graph",
                        variable=var, value=6)
    R6.config(font=('Arial', 10))
    gen_btn = tk.Button(
        frame2,
        width=15,
        text='Generate',
        font=ff,
        relief=tk.SOLID,
        cursor='hand2',
        command=gen
    )

    gen_btn.place(x=725, y=100)
    R1.place(x=45, y=50)
    R2.place(x=45, y=100)
    R3.place(x=45, y=150)
    R4.place(x=325, y=100)
    R5.place(x=325, y=150)
    R6.place(x=520, y=150)

    # BUY STOCK
    buyLabel = tk.Label(frame3, text="Buy Stocks")
    buyLabel.config(font=('Courier', 14, 'bold', 'underline'), fg='black')
    buyLabel.place(x=350, y=15)

    BsymbolLabel = tk.Label(frame3, text="Symbol:")
    BsymbolLabel.config(font=('Courier', 12, 'bold'), fg='black')
    BsymbolLabel.place(x=370, y=55)
    BsymbolEntry = tk.Entry(frame3, bd=2, textvariable=Bsym, width=10)
    BsymbolEntry.place(x=450, y=55)

    volLabel = tk.Label(frame3, text="Volume:")
    volLabel.config(font=('Courier', 12, 'bold'), fg='black')
    volLabel.place(x=370, y=155)

    volEntry = tk.Entry(frame3, bd=2, textvariable=vols, width=10)
    volEntry.place(x=450, y=155)

    buy_btn = tk.Button(
        frame3,
        width=15,
        text='Buy',
        font=ff,
        relief=tk.SOLID,
        cursor='hand2',
        command=buy
    )

    buy_btn.place(x=725, y=100)

    # PORTFOLIO
    temp=[]
    sortable = tk.BooleanVar(root, False)
    drag_row = tk.BooleanVar(root, False)
    drag_col = tk.BooleanVar(root, False)
    table = Table(frame4,sortable=sortable.get(), drag_cols=drag_col.get(),
                    drag_rows=drag_row.get(), height=6)
    mycursor.execute("select * from Buy where UserName='"+str(u[0][4])+"'")
    result = mycursor.fetchall()
    num_fields = len(mycursor.description)
    field_names = [i[0] for i in mycursor.description]
    table.config(columns=field_names)
    
    if len(result) == 0:
        noLabel = tk.Label(frame4, text="No Stocks In Portfolio")
        noLabel.config(font=('Courier', 14, 'bold', 'underline'), fg='black')
        noLabel.place(x=350, y=15)
        
    
    for x in field_names:
        table.heading(x, text=x)
        table.column(x, width=100, stretch=False)

    for x in result:
        for a in x:
            temp.append(a)

        table.insert("", 'end', text="L1", values=tuple(temp))
        temp = []

    sx = tk.Scrollbar(frame4, orient='horizontal', command=table.xview)
    sy = tk.Scrollbar(frame4, orient='vertical', command=table.yview)
    table.configure(yscrollcommand=sy.set, xscrollcommand=sx.set)
    table.grid(sticky='ewns')
    sx.grid(row=1, column=0, sticky='ew')
    sy.grid(row=0, column=1, sticky='ns')
    frame4.update_idletasks()
    # toggle table properties

    def toggle_sort():
        table.config(sortable=sortable.get())

    def toggle_drag_col():
        table.config(drag_cols=drag_col.get())

    def toggle_drag_row():
        table.config(drag_rows=drag_row.get())

    frame = tk.Frame(frame4)
    tk.Checkbutton(frame, text='sortable', variable=sortable,
                    command=toggle_sort).pack(side='left')
    tk.Checkbutton(frame, text='drag columns', variable=drag_col,
                    command=toggle_drag_col).pack(side='left')
    tk.Checkbutton(frame, text='drag rows', variable=drag_row,
                    command=toggle_drag_row).pack(side='left')
    frame.grid()
    
    
    proLabel = tk.Label(frame5, text="Your Profile")
    proLabel.config(font=('Courier', 14, 'bold', 'underline'), fg='black')
    proLabel.place(x=350, y=15)
    
    nameLabel = tk.Label(frame5, text="Name:")
    nameLabel.config(font=('Courier', 14, 'bold', 'underline'), fg='black')
    nameLabel.place(x=30, y=55)
    name = tk.Label(frame5, text=str(u[0][1])+" " + str(u[0][2]))
    name.config(font=('Courier', 13, 'bold'), fg='black')
    name.place(x=110, y=55)
    
    mailLabel = tk.Label(frame5, text="Email:")
    mailLabel.config(font=('Courier', 14, 'bold', 'underline'), fg='black')
    mailLabel.place(x=30, y=105)
    mail = tk.Label(frame5, text=str(u[0][7]))
    mail.config(font=('Courier', 13, 'bold'), fg='black')
    mail.place(x=110, y=105)
    
    mobiLabel = tk.Label(frame5, text="Ph No:")
    mobiLabel.config(font=('Courier', 14, 'bold', 'underline'), fg='black')
    mobiLabel.place(x=30, y=155)
    mobi = tk.Label(frame5, text=str(u[0][8]))
    mobi.config(font=('Courier', 13, 'bold'), fg='black')
    mobi.place(x=110, y=155)
    
    addrLabel = tk.Label(frame5, text="Address:")
    addrLabel.config(font=('Courier', 14, 'bold', 'underline'), fg='black')
    addrLabel.place(x=300, y=155)
    addr = tk.Label(frame5, text=str(u[0][6]))
    addr.config(font=('Courier', 13, 'bold'), fg='black')
    addr.place(x=400, y=155)
    
    
    
    
    
    
    
    
    root.mainloop()
