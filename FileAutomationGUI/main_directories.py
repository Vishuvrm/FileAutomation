import os

from .logbase import logger
import win32api
import tkinter as tk
from tkinter import ttk

class GetDirectories:
    def __init__(self, root, tk, ttk):
        self.root = root
        
        # initialize data
        self.main_dir = ["dir"]
        self.first_value = "dir"
        self.drives = win32api.GetLogicalDriveStrings()
        self.drives = self.drives.split('\000')[:-1]
        self.main_dir.extend(self.drives)
        self.tk = tk
        self.ttk = ttk
        self.text_dir = None

        # set up variable
        self.option_var = self.tk.StringVar(root)
        self.dir = None
        self.custom_dir = self.tk.StringVar()

        # Some flag variables:
        self.r1 = None
        self.r2 = None

        # create widget
        self.create_wigets()

    def create_wigets(self):
        if self.text_dir:
            if not self.text_dir in set(self.main_dir):
                self.main_dir.append(self.text_dir)
                # self.first_value = self.text_dir
                self.dir = self.text_dir


        option_menu = self.ttk.OptionMenu(
            self.root,
            self.option_var,
            self.first_value,
            *self.main_dir,
            command=self.option_changed)
        option_menu.config(width=18)


        # Search box
        self.search = self.tk.Entry(self.root, text="Search", bd=2, font="Calibri 10", width=23, textvariable=self.custom_dir)
        # Add text in Entry box
        self.search.delete(0, "end")
        self.search.insert(0, "Dir:")
        self.search.bind("<Button-1>", self.click)  # Left click
        self.search.bind("<Leave>", self.leave)
        self.search.bind('<Return>', self.callback)

        # Pack the widgets
        option_menu.place(x=0, y=423)
        self.search.place(x=0, y=398)

    def option_changed(self, *args):
        logger.create_log(logger_name="main_directories.py",
                          message=f"You selected ({self.option_var.get()}) from the directories dropdown on the home page",
                          message_level="INFO")

        if self.option_var.get() == "dir":
            self.dir = None

        elif self.option_var.get() != "dir":
            # if self.option_var.get()
            self.dir = self.option_var.get()

        elif self.text_dir == "Dir:" or not self.text_dir:
            self.dir = None

        elif self.text_dir:
            self.dir = self.text_dir

# call function when we click on entry box
    def click(self, *args):
        logger.create_log(logger_name="main_directories.py", message="You clicked the directory search bar on the home page.", message_level="INFO")
        self.text_dir = self.search.get().strip(" ")
        if self.text_dir == 'Dir:':
            self.search.delete(0, 'end')
        self.root.focus()


# call function when we leave entry box
    def leave(self, *args):
        logger.create_log(logger_name="main_directories.py", message="You hovered over the directory search bar on the main window.", message_level="INFO")
        self.text_dir = self.search.get().strip(" ")
        if self.text_dir == "":
            self.search.delete(0, 'end')
            self.search.insert(0, 'Dir:')
            self.root.focus()

# Call function, when pressed Enter key
    def callback(self, event):
        self.text_dir = self.search.get().strip(" ")
        logger.create_log(logger_name="app.py", message=f"You entered ({self.text_dir}) directory in the main window directory search bar.", message_level="INFO")

        if (self.text_dir=="Dir:" or not self.text_dir or not(os.path.exists(self.text_dir))):
            if self.r1:
                self.r1.destroy()
            if self.r2:
                self.r2.destroy()
            self.r2 = self.tk.Label(self.root, text=f"{self.text_dir[:6]}...Invalid Address!", foreground="red")
            self.r2.place(x=0, y=450)

        else:
            if self.r2:
                self.r2.destroy()
            self.r1 = self.tk.Label(self.root, text=f"{self.text_dir[:6]}... added!", foreground="blue")
            self.r1.place(x=0, y=450)

            ########### PROCESS #############
            logger.create_log(logger_name="app.py",
                              message=f"The directory {self.text_dir} is added to the search path...",
                              message_level="INFO")
            self.option_changed()
            self.create_wigets()

            ########### PROCESS END #########

if __name__ == "__main__":
    root = tk.Tk()

    GetDirectories(root, tk, ttk)
    tk.mainloop()