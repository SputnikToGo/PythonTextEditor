__author__ = 'miika'
import tkinter as tk
from tkinter import Menu
import tkinter.scrolledtext as tkst
from tkinter import filedialog
from tkinter import messagebox

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

#Tehdään valikkoriville komennot
def open_command():
        file = filedialog.askopenfile(parent=win, mode='rb', title='Select a file')
        if file != None:
            contents = file.read()
            editArea.insert('1.0', contents)
            file.close()

#def save_command(self):
#        file = filedialog.asksaveasfile(mode='w')
#        if file != None:
#            data = self.editArea.get('1,0', END+ '-1c')
#            file.write(data)
#            file.close()

def exit_command():
    if messagebox.askokcancel("Quit", "Do you really want to guit?"):
        win.destroy()
#Lopetetaan komentojen tekeminen

# Luodaan valikkorivi nimeltä Menu
menu = Menu(win)
win.config(menu=menu)
filemenu =  Menu(menu)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New")
filemenu.add_command(label="Open...", command=open_command())
filemenu.add_command(label="Save")
filemenu.add_separator()
filemenu.add_command(label="Exit", command = exit_command())
#Lopetetaan valikkorivin luominen

editArea.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
editArea.insert(tk.INSERT,
"""\
""")

editArea.pack()
win.mainloop()