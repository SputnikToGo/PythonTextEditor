__author__ = 'miika'
import tkinter as tk
from tkinter import Menu
import tkinter.scrolledtext as tkst
from tkinter import filedialog
from tkinter import messagebox
from tkinter.filedialog import asksaveasfile

#Aloitetaan komentojen tekeminen

def openCommand():
    file = tk.filedialog.askopenfile(parent=root,mode='rb', title='Valitse tiedosto')
    if file !=None:
        contents = file.read()
        textPad.insert('1.0',contents)
        file.close()

#def saveCommand(self):


def exitCommand():
    if tk.messagebox.askokcancel("Poistu", "Haluatko todella poistua?"):
        root.destroy()
#Lopetetaan komentojen tekeminen



#Tässä kohtaa luodaan tekstieditori
root = tk.Tk(className= "Tekstieditori")
textPad = tkst.ScrolledText(root, width=100, height=25)

textPad.bind()

# Luodaan valikkorivi nimeltä Menu
menu = Menu(root)
root.config(menu=menu)


filemenu =  Menu(menu)
menu.add_cascade(label="Tiedosto", menu=filemenu)
filemenu.add_command(label="Avaa..", command=openCommand)
filemenu.add_command(label="Tallenna")
filemenu.add_separator()
filemenu.add_command(label="Poistu", command = exitCommand)
#Lopetetaan valikkorivin luominen



textPad.pack()
root.mainloop()




