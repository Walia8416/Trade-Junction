import tkinter as tk
from tkinter import ttk
from ttkwidgets import Table
import requests


def stockInfo(choice, sym):

    if choice == 1:

        url = f'https://www.alphavantage.co/query?function=OVERVIEW&symbol={sym}&apikey=HYGXZH658SIG5BL0'
        r = requests.get(url)
        data = r.json()
        cols = []
        temp = []

        if (len(data) == 1):
            tk.messagebox.showerror('Error', 'Please Wait!')
        else:
            root = tk.Tk()
            root.columnconfigure(0, weight=1)
            root.rowconfigure(0, weight=1)
            root.title(sym)
            style = ttk.Style(root)
            style.theme_use('alt')
            sortable = tk.BooleanVar(root, False)
            drag_row = tk.BooleanVar(root, False)
            drag_col = tk.BooleanVar(root, False)

            for x in data:
                cols.append(x)
            table = Table(root, columns=cols, sortable=sortable.get(), drag_cols=drag_col.get(),
                          drag_rows=drag_row.get(), height=6)
        
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
            
