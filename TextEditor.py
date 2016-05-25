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
from tkinter import Entry
from tkinter import Toplevel
from tkinter import Button
from tkinter.filedialog import asksaveasfile
from fileSystem import File

def main():
    editor = Editor();

class Editor:
    def __init__(self):
        # Initialize the text editor
        self.root = tk.Tk(className= 'Tekstieditori')

        self.textpad = tkst.ScrolledText(self.root, width=100, height=36, highlightthickness=0)
        self.textpad.config(font=('tkDefaultFont',16,'normal'))
        self.textpad.pack(padx=10,pady=10)

        self.file = {}

        #Luodaan valikkorivi nimeltä Menu
        self.menu = Menu(self.root)
        self.filemenu =  Menu(self.menu)
        self.file_menu_conf()

        self.sel_index = [0,1]

        self.event_config()

        self.root.mainloop()

    # File open dialog
    def open(self):
        # Ask the user for a file to open
        userinput = tk.filedialog.askopenfilename(parent=self.root, title='Valitse tiedosto')

        # Wait for user input
        if userinput is not None:

            # Use the fileSystem class for all file operations
            self.file = File(userinput)
            contents = self.file.read()

            # Empty the editor
            self.textpad.delete('1.0',tk.END+'-1c')

            # Insert the contents to the editor
            self.textpad.insert('1.0',contents)

            # Populate with existing tags
            self.populate_tags()

    def file_menu_conf(self):
        self.root.config(menu=self.menu)
        self.menu.add_cascade(label="Tiedosto", menu=self.filemenu)
        self.filemenu.add_command(label="Avaa..", command=self.open)
        self.filemenu.add_command(label="Tallenna", command=self.save)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Poistu", command = self.exit)

    def create_window(self):
        self.t = Toplevel(self.root)
        self.t.title("Lisää tägi")

        self.e = Entry(self.t)
        self.e.pack()
        self.get_index()

        self.b = Button(self.t, text="Lisää tägi", command = self.add_tag(self.e.get()))
        self.b.pack()

    # Saving the original file (not the tags)
    def save(self):
        # Open the file dialog
        userinput = tk.filedialog.asksaveasfilename()

        # Wait for user input
        if userinput is not None:

            # Get text editor contents
            data = self.textpad.get('1.0', tk.END+'-1c')

            # Write data to file
            self.file.write(data)


    def exit(self):
        self.root.protocol('WM_DELETE_WINDOW', self.exit)
        if tk.messagebox.askokcancel("Poistu", "Haluatko todella poistua?"):
            self.root.destroy()


    #Ponnahdusikkunan eventti, kommentoitu ulos, koska ihan tärkeitä juttuja vielä sisältää (TRY!!! :3)
    #def popup_window(self, event):
    #    try:
    #        self.popup.tk_popup(event.x_root, event.y_root, 0)
    #        print(self.textpad.index("sel.first"))
    #        print(self.textpad.index("sel.last"))
    #
    #        self.textpad.selection_clear()
    #    finally:
    #        self.popup.grab_release()

    def populate_tags(self):
        for tag in self.file.readtags():
            self.textpad.tag_add(tag["tag"],tag["index"][0],tag["index"][1])
            self.textpad.tag_config(tag["tag"], background="yellow")

    def add_tag(self,description):
        self.textpad.tag_add(description,self.sel_index[0],self.sel_index[1])
        self.textpad.tag_config(description, background="yellow")
        self.file.tag(description,self.sel_index)

    def get_index(self):
        try:
            self.sel_index = [self.textpad.index("sel.first"),self.textpad.index("sel.last")]

    def event_config(self):
        self.textpad.bind("<Button-3>", self.create_window)
        # Remove unnecessary copy and paste on second mouse click
        self.root.bind_class("Text", sequence='<Button-2>', func=self.create_window)
        self.root.bind_class("Text", sequence='<Button-3>', func=self.create_window)


if __name__ == '__main__':
  main()
