__author__ = 'miika'
import tkinter as tk
from tkinter import Menu
import tkinter.scrolledtext as tkst

win = tk.Tk()
frame1 = tk.Frame(
    master = win,
#   bg = '#808000'
)
frame1.pack(fill='both', expand='yes')
editArea = tkst.ScrolledText(
    master = frame1,
    wrap   = tk.WORD,
    width  = 20,
    height = 10
)
# Don't use widget.place(), use pack or grid instead, since
# They behave better on scaling the window -- and you don't
# have to calculate it manually!
editArea.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
# Adding some text, to see if scroll is working as we expect it
editArea.insert(tk.INSERT,
"""\
""")


win.mainloop()