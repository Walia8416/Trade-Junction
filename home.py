import tkinter as tk
from tkinter import ttk
import requests

from stockInfo import stockInfo


f = open('stocks.txt', 'r')
ff = ('Times', 12)


def gen():

    if len(sym.get()) == 0:
        tk.messagebox.showerror('Error', 'Please Enter Symbol!')

    else:
        stockInfo(var.get(),sym.get())
        

def homeScreen(user):
    global sym, var
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
            url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=BSE:{stock}&apikey=Y4OVHTX2WGRVU8H6"
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

    root.mainloop()
