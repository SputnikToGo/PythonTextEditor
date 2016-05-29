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
    """ Create the main editor,
        and add it to the main loop.
    """
    editor = Editor();
    editor.root.mainloop()

class Editor:
    def __init__(self):
        # Initialize the text editor
        self.root = tk.Tk(className= 'Tekstieditori')

        # Text editor text area
        self.textpad = tkst.ScrolledText(self.root, width=100, height=36, highlightthickness=0)
        self.textpad.config(font=('tkDefaultFont',16,'normal'))
        self.textpad.pack(padx=10,pady=10)

        # Create a file menu in menu bar
        self.menu = Menu(self.root)
        self.filemenu = Menu(self.menu)
        self.file_menu_conf()

        # Initialize the selection index class variable
        self.sel_index = [0,1]

        # Configurate click events
        self.event_config()

    def open(self):
        """ File open dialog, used via a file menu in menu bar

            TODO(maybe): open when no file is opened
        """
        # Ask the user for a file to open
        userinput = tk.filedialog.askopenfilename(parent=self.root, title='Valitse tiedosto')

        # Wait for user input
        if userinput is None or userinput is "":
            self.open()
        else:
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
        """ File menu configuration,
            add the menu buttons.
        """
        self.root.config(menu=self.menu)
        self.menu.add_cascade(label="Tiedosto", menu=self.filemenu)
        self.filemenu.add_command(label="Avaa..", command=self.open)
        self.filemenu.add_command(label="Tallenna", command=self.save)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Poistu", command = self.exit)

    def create_window(self,event):
        """ Popup window which is used for adding and reading tags.
            Opened with a right click on selected text, contains an
            entry field, which shows existing tags, and can be used
            to add new ones.
        """
        # Create a new popup window
        self.t = Toplevel(self.root)
        self.t.title("Lisää tägi")

        # Tag entry field
        self.e = Entry(self.t)
        self.e.pack()

        # Get the selection index before inserting its tags in the entry field
        self.get_index()

        # Tag submit button
        self.b = Button(self.t, text="Lisää tägi", command=self.entry_callback)
        self.b.pack()

        # Get existing tags
        existing_tags = self.file.get_tags_by_index(self.sel_index)

        # If there are existing tags, show them on opening the entry field
        if existing_tags and len(existing_tags)>1:
            self.e.insert(0, existing_tags)
        else:
            # Greeting, if no tags are present
            self.e.insert(0, "No tags yet! Write one :)")


    def save(self):
        """ Save the original file or create a new one,
            if there's no file opened already.
        """
        # Open the file dialog
        userinput = tk.filedialog.asksaveasfilename()

        # Wait for user input
        if userinput is not None:

            # Initialize file if nonexistent
            if not self.file.path:
                self.file = File(userinput)

            # Get text editor contents
            data = self.textpad.get('1.0', tk.END+'-1c')

            # Write data to file
            self.file.write(data)


    def exit(self):
        """ Exit command, which is
            called whenever user
            wants to close the whole editor.
        """
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
        """ Get existing tags from the tag
            file, and print them with tkinter
            tag_add as yellow highlighted
            areas in the text.
        """
        for tag in self.file.readtags():
            if len(tag)>0:
                for contents in tag["tag"]:
                    self.textpad.tag_add(tag[contents],tag["index"][0],tag["index"][1])
                    self.textpad.tag_config(tag[contents], background="yellow")

    def entry_callback(self):
        """ Callback event for adding a tag.
            Called when the tag submit button
            is pressed, because tkinter button
            event can't have any input.
        """
        self.add_tag(self.e.get())

    def add_tag(self, description):
        """ GUI implementation of tagging.
            Uses the filesystem for saving
            tags to a file, and saves new tags
            graphically with tkinter tag_add()
        """
        try:
            # Add the tag(s) graphically to the text
            self.textpad.tag_add(description,self.sel_index[0],self.sel_index[1])
            self.textpad.tag_config(description, background="yellow")

            # Initialize file if nonexistent
            if not self.file.path:
                self.save()

            # Add the tag(s) to original file's tag file in data/
            self.file.tag(description,self.sel_index)
        except Exception:
            # When something goes wrong...
            print("...Whoooops...")

    def get_index(self):
        """ Get the indeces of selected text.
            Used whenever and before any new
            tags are added.
        """
        try:
            self.sel_index = [self.textpad.index("sel.first"),self.textpad.index("sel.last")]
        except tk.TclError:
            # Error, which is raised when no selection indeces are present.
            print("You need to select something before getting selection index!")

    def event_config(self):
        #self.textpad.bind("<Button-2>", self.create_window)
        # Remove unnecessary copy and paste on second mouse click
        self.root.bind_class("Text", sequence='<Button-2>', func=self.create_window)


if __name__ == '__main__':
  main()
