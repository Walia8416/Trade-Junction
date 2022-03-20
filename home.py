import tkinter as tk
from tkinter import ttk


def homeScreen():
    root = tk.Tk()
    root.geometry('1000x600')
    root.title('Trade Junction')
    
    
    headLabel = tk.Label(root, text="Trade Junction")
    headLabel.config(font=('Courier', 29, 'bold', 'underline'), fg='black')
    headLabel.place(x=350, y=20)
    
    notebook = ttk.Notebook(root)
    notebook.pack(pady=10, expand=True)
    frame1 = ttk.Frame(notebook, width=1000, height=380)
    frame2 = ttk.Frame(notebook, width=1000, height=380)
    frame3 = ttk.Frame(notebook, width=1000, height=380)
    frame4 = ttk.Frame(notebook, width=1000, height=380)
    frame5 = ttk.Frame(notebook, width=1000, height=380)
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

    root.mainloop()
