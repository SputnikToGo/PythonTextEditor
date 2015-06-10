__author__ = 'miika'
import tkinter as tk
from tkinter import Menu
import tkinter.scrolledtext as tkst

win = tk.Tk()
win.title("Text editor")
frame1 = tk.Frame(
    master = win,
#    bg = '#808000'
)

# Luodaan tekstikenttä
frame1.pack(fill='both', expand='yes')
editArea = tkst.ScrolledText(
    master = frame1,
    wrap   = tk.WORD,
    width  = 100,
    height = 25
)

# Luodaan valikkorivi nimeltä Menu
menu = Menu(win)
win.config(menu=menu)
filemenu =  Menu(menu)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New")
filemenu.add_command(label="Open")
filemenu.add_command(label="Save")
filemenu.add_separator()
filemenu.add_command(label="Exit")
#Lopetetaan valikkorivin luominen

editArea.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
editArea.insert(tk.INSERT,
"""\
""")


win.mainloop()