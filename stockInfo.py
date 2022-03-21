from ttkwidgets import Table
import tkinter as tk
from tkinter import ttk
import requests
import matplotlib.pyplot as plt


def delete_command(tree,root):
    print('sdf')
    tree.destroy()
    root.destroy()
    

def fetchData(url, keys, sym):

    r = requests.get(url)
    data = r.json()
    cols = []
    temp = []

    if (len(data) == 1):
        tk.messagebox.showerror('Error', 'Please Wait!')
    else:
        for rec in data[keys]:
            for names in rec:
                if names not in cols:
                    cols.append(names)
        table.config(columns=cols)
        for x in cols:
            table.heading(x, text=x)
            table.column(x, width=100, stretch=False)

        for x in data[keys]:
            for vals in x:
                temp.append(x[vals])

            table.insert("", 'end', text="L1", values=tuple(temp))
            temp = []

        sx = tk.Scrollbar(root, orient='horizontal', command=table.xview)
        sy = tk.Scrollbar(root, orient='vertical', command=table.yview)
        table.configure(yscrollcommand=sy.set, xscrollcommand=sx.set)
        table.grid(sticky='ewns')
        sx.grid(row=1, column=0, sticky='ew')
        sy.grid(row=0, column=1, sticky='ns')
        root.update_idletasks()
        # toggle table properties

        def toggle_sort():
            table.config(sortable=sortable.get())

        def toggle_drag_col():
            table.config(drag_cols=drag_col.get())

        def toggle_drag_row():
            table.config(drag_rows=drag_row.get())

        frame = tk.Frame(root)
        tk.Checkbutton(frame, text='sortable', variable=sortable,
                       command=toggle_sort).pack(side='left')
        tk.Checkbutton(frame, text='drag columns', variable=drag_col,
                       command=toggle_drag_col).pack(side='left')
        tk.Checkbutton(frame, text='drag rows', variable=drag_row,
                       command=toggle_drag_row).pack(side='left')
        frame.grid()
        root.geometry('400x200')
        root.protocol("WM_DELETE_WINDOW",lambda: delete_command(table,root))
        root.mainloop()
        return None


def stockInfo(win,choice, sym):
    global root,table,drag_col,drag_row,sortable
    root = tk.Toplevel(win)
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)
    root.title(sym)
    
    sortable = tk.BooleanVar(root, False)
    drag_row = tk.BooleanVar(root, False)
    drag_col = tk.BooleanVar(root, False)
    table = Table(root,sortable=sortable.get(), drag_cols=drag_col.get(),
                    drag_rows=drag_row.get(), height=6)
   
    if choice == 1:

        url = f'https://www.alphavantage.co/query?function=OVERVIEW&symbol={sym}&apikey=HYGXZH658SIG5BL0'
        r = requests.get(url)
        data = r.json()
        cols = []
        temp = []

        if (len(data) == 1):
            tk.messagebox.showerror('Error', 'Please Wait!')
        else:
            

            for x in data:
                cols.append(x)
            
            table.config(columns=cols)
            for x in cols:
                table.heading(x, text=x)
                table.column(x, width=100, stretch=False)

            for x in data:
                temp.append(data[x])

            table.insert("", 'end', text="L1", values=tuple(temp))
            sx = tk.Scrollbar(root, orient='horizontal', command=table.xview)
            sy = tk.Scrollbar(root, orient='vertical', command=table.yview)
            table.configure(yscrollcommand=sy.set, xscrollcommand=sx.set)
            table.grid(sticky='ewns')
            sx.grid(row=1, column=0, sticky='ew')
            sy.grid(row=0, column=1, sticky='ns')
            root.update_idletasks()
            # toggle table properties

            def toggle_sort():
                table.config(sortable=sortable.get())

            def toggle_drag_col():
                table.config(drag_cols=drag_col.get())

            def toggle_drag_row():
                table.config(drag_rows=drag_row.get())

            frame = tk.Frame(root)
            tk.Checkbutton(frame, text='sortable', variable=sortable,
                           command=toggle_sort).pack(side='left')
            tk.Checkbutton(frame, text='drag columns', variable=drag_col,
                           command=toggle_drag_col).pack(side='left')
            tk.Checkbutton(frame, text='drag rows', variable=drag_row,
                           command=toggle_drag_row).pack(side='left')
            frame.grid()
            root.geometry('400x200')

            root.mainloop()
            return None

    elif choice == 2:

        fetchData(
            f'https://www.alphavantage.co/query?function=INCOME_STATEMENT&symbol={sym}&apikey=HYGXZH658SIG5BL0', 'quarterlyReports', sym)
        return None

    elif choice == 3:

        fetchData(
            f'https://www.alphavantage.co/query?function=BALANCE_SHEET&symbol={sym}&apikey=HYGXZH658SIG5BL0', 'quarterlyReports', sym)
        return None
    elif choice == 4:

        fetchData(
            f'https://www.alphavantage.co/query?function=CASH_FLOW&symbol={sym}&apikey=HYGXZH658SIG5BL0', 'quarterlyReports', sym)
        return None

    elif choice == 5:

        fetchData(
            f'https://www.alphavantage.co/query?function=EARNINGS&symbol={sym}&apikey=HYGXZH658SIG5BL0', 'quarterlyEarnings', sym)
        return None
    
    else:
        
        url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={sym}&apikey=Y4OVHTX2WGRVU8H6"
        r = requests.get(url)
        data = r.json()
        a = data["Time Series (Daily)"]
        c = 0
        x = []
        y = []
        for date in a:
            for value in a[date]:
                x.append(date)
                y.append(a[date]['4. close'])
        
  
        
        
        
        plt.xlabel("Date")
        plt.ylabel("Price")
        plt.title(sym)
        plt.plot(x,y)
        plt.show()
        
