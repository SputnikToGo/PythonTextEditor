# -*- coding: utf-8 -*-
__author__ = 'Miika Länsi-Seppänen, Jani Anttonen'
# Add version check for development
import platform
print(platform.python_version())

# Imports
import tkinter as tk
from tkinter import Menu
import tkinter.scrolledtext as tkst
from tkinter import filedialog
from tkinter import messagebox
from tkinter.filedialog import asksaveasfile
from fileSystem import File

def main():
    editor = Editor();

class Editor:
    def __init__(self):
        # Initialize the text editor
        self.root = tk.Tk(className= 'Tekstieditori')
        self.textPad = tkst.ScrolledText(self.root, width=150, height=50, highlightthickness=0)
        self.file = {}

        #Luodaan valikkorivi nimeltä Menu
        self.menu = Menu(self.root)
        self.filemenu =  Menu(self.menu)

        #Luodaan ponnahdusikkuna
        self.popup = Menu(self.root, tearoff=0)

        self.config()

    # File open dialog
    def openCommand(self):

        # Ask the user for a file to open
        userinput = tk.filedialog.askopenfilename(parent=self.root, title='Valitse tiedosto')

        # Wait for user input
        if userinput is not None:

            # Use the fileSystem class for all file operations
            self.file = File(userinput)
            contents = self.file.read()

            # Empty the editor
            self.textPad.delete('1.0',tk.END+'-1c')

            # Insert the contents to the editor
            self.textPad.insert('1.0',contents)

            # Populate with existing tags
            self.populate_tags()


    # Saving the original file (not the tags)
    def saveCommand(self):

        # Open the file dialog
        userinput = tk.filedialog.asksaveasfilename()

        # Wait for user input
        if userinput is not None:

            # Get text editor contents
            data = self.textPad.get('1.0', tk.END+'-1c')

            # Write data to file
            self.file.write(data)


    def exitCommand(self):
        if tk.messagebox.askokcancel("Poistu", "Haluatko todella poistua?"):
            self.root.destroy()

    #Ponnahdusikkunan eventti
    def popupWindow(self, event):
        try:
            self.popup.tk_popup(event.x_root, event.y_root, 0)
            self.add_tag("ebin", [self.textPad.SEL_FIRST, self.textPad.SEL_LAST])
            print(self.textPad.index("sel.first"))
            print(self.textPad.index("sel.last"))
            self.textPad.selection_clear()
        finally:
            self.popup.grab_release()

    def populate_tags(self):
        for tag in self.file.readtags():
            self.textPad.tag_add(tag["tag"],tag["index"][0],tag["index"][1])

    def add_tag(self,description,index):
        self.textPad.tag_add(description,index[0],index[1])
        self.file.tag(description,index)

    def config(self):
        self.root.config(menu=self.menu)
        self.menu.add_cascade(label="Tiedosto", menu=self.filemenu)
        self.filemenu.add_command(label="Avaa..", command=self.openCommand)
        self.filemenu.add_command(label="Tallenna", command=self.saveCommand)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Poistu", command = self.exitCommand)
        self.root.protocol('WM_DELETE_WINDOW', self.exitCommand)
        self.popup.add_command(label="Lisää tägit")
        self.popup.add_command(label="Muokkaa tägiä")
        self.popup.add_separator()
        self.popup.add_command(label="Poista tägi")
        self.textPad.bind("<Button-2>", self.popupWindow)
        self.textPad.pack()
        self.root.mainloop()

        # Remove unnecessary copy and paste on second mouse click
        self.root.bind_class("Text", sequence='<Button-2>', func=self.popupWindow)


if __name__ == '__main__':
  main()
