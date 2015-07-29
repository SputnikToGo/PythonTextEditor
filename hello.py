__author__ = 'miika'
import tkinter as tk
from tkinter import Menu
import tkinter.scrolledtext as tkst
from tkinter import filedialog
from tkinter import messagebox

#Tässä kohtaa luodaan tekstieditori
root = tk.Tk(className= "Tekstieditori")
textPad = tkst.ScrolledText(root, width=100, height=50)

#Aloitetaan komentojen tekeminen
def open_command():
    file = tk.filedialog.askopenfile(parent=root,mode='rb', title='Valitse tiedosto')
    if file !=None:
        contents = file.read()
        textPad.insert('1.0',contents)
        file.close()

def save_command(self):
    file = tk.filedialog.asksaveasfile(mode='W')
    if file != None:
        data = self.textPad.get('1,0', END+'-1c')
        file.write(data)
        file.close()


def exit_command():
    if tk.messagebox.askokcancel("Poistu", "Haluatko todella poistua?"):
        root.destroy()
#Lopetetaan komentojen tekeminen

# Luodaan valikkorivi nimeltä Menu
menu = Menu(root)
root.config(menu=menu)
filemenu =  Menu(menu)
menu.add_cascade(label="Tiedosto", menu=filemenu)
filemenu.add_command(label="Uusi")
filemenu.add_command(label="Avaa..", command=open_command())
filemenu.add_command(label="Tallenna")
filemenu.add_separator()
filemenu.add_command(label="Poistu", command = exit_command())
#Lopetetaan valikkorivin luominen


textPad.pack()
root.mainloop()