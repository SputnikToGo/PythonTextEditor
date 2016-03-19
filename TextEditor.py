__author__ = 'miika'
import tkinter as tk
from tkinter import Menu
import tkinter.scrolledtext as tkst
from tkinter import filedialog
from tkinter import messagebox
from tkinter.filedialog import asksaveasfile
from fileSystem import File

# Initialize the text editor
root = tk.Tk(className= 'Tekstieditori')
textPad = tkst.ScrolledText(root, width=150, height=50)


# File open dialog
def openCommand():

    # Ask the user for a file to open
    userinput = tk.filedialog.askopenfilename(parent=root, title='Valitse tiedosto')

    # Wait for user input
    if userinput is not None:

        # Use the fileSystem class for all file operations
        file = File(userinput)
        contents = file.read()

        # Empty the editor
        textPad.delete('1.0',tk.END+'-1c')

        # Insert the contents to the editor
        textPad.insert('1.0',contents)


# Saving the original file (not the tags)
def saveCommand():

    # Open the file dialog
    userinput = tk.filedialog.asksaveasfilename()

    # Wait for user input
    if userinput is not None:

        # Open a file object
        file = File(userinput)

        # Get text editor contents
        data = textPad.get('1.0', tk.END+'-1c')

        # Write data to file
        file.write(data)


def exitCommand():
    if tk.messagebox.askokcancel("Poistu", "Haluatko todella poistua?"):
        root.destroy()

#Ponnahdusikkunan eventti
def popupWindow(event):
    try:
        popup.tk_popup(event.x_root, event.y_root, 0)
        print(textPad.index("sel.first"))
        print(textPad.index("sel.last"))
    finally:
        popup.grab_release()




#Luodaan valikkorivi nimeltä Menu
menu = Menu(root)
root.config(menu=menu)
filemenu =  Menu(menu)
menu.add_cascade(label="Tiedosto", menu=filemenu)
filemenu.add_command(label="Avaa..", command=openCommand)
filemenu.add_command(label="Tallenna", command=saveCommand)
filemenu.add_separator()
filemenu.add_command(label="Poistu", command = exitCommand)
root.protocol('WM_DELETE_WINDOW', exitCommand)

#Luodaan ponnahdusikkuna
popup = Menu(root, tearoff=0)
popup.add_command(label="Lisää tägit")
popup.add_command(label="Muokkaa tägiä")
popup.add_separator()
popup.add_command(label="Poista tägi")
textPad.bind("<Button-2>", popupWindow)


textPad.pack()
root.mainloop()