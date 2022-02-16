import os

from .logbase import logger

import tkinter as tk
from tkinter import ttk

class SearchExt:
    def __init__(self, child, root, tk, ttk):

        self.root = root
        self.child = child
        # initialize data
        self.extension = ["None",'.txt', '.docx', ".pdf", ".mp3", ".mp4",".png", ".jpg", "png/jpg", ".xlsx"]
        self.tk = tk
        self.ttk = ttk
        # set up variable
        self.option_var = self.tk.StringVar(root)
        self.dst = self.tk.StringVar()
        self.file = None
        self.ext = self.extension[0]
        self.file_text = None
        self.output = None
        self.paddings = {'padx': 5, 'pady': 5}
        self.combined = None
        self.text_ext = None
        self.custom_dir = self.tk.StringVar()

        # Some flag variables:
        self.r1 = None
        self.r2 = None
        self.use_option = True
        self.option_menu = None

        # create widget
        self.create_wigets()

    def create_wigets(self):
        if self.text_ext:
            if not self.text_ext in set(self.extension):
                self.extension.append(self.text_ext)
                self.ext = self.text_ext
                self.option_menu.destroy()

        # padding for widgets using the grid layout

        # option menu
        self.option_menu = self.ttk.OptionMenu(
            self.root,
            self.option_var,
            self.extension[0],
            *self.extension,
            command=self.option_changed)


        # Search box
        self.search = self.tk.Entry(self.root, text="Search", bd=2, font="Calibri 10", width=10,
                                    textvariable=self.custom_dir)
        # Add text in Entry box
        self.search.delete(0, "end")
        self.search.insert(0, "add .ext")
        self.search.bind("<Button-1>", self.click)  # Left click
        self.search.bind("<Leave>", self.leave)
        self.search.bind('<Return>', self.callback)

        # label
        self.label = self.ttk.Label(self.root,  text='Search file with extension:')

        # output label
        self.output_label = self.ttk.Label(self.root, foreground='red')

        # Pack the widgets
        self.output_label.place(x = 300, y = 500)
        # self.option_menu.pack(side=self.tk.BOTTOM, **self.paddings)
        self.option_menu.place(x=380, y=458)
        # label.pack(side=self.tk.BOTTOM, **self.paddings)
        self.label.place(x=300, y=438)
        self.search.place(x=298, y=458)

    def option_changed(self, *args):

        logger.create_log(logger_name="home_page_ext.py",
                          message=f"You selected ({self.option_var.get()}) extension from the extensions dropdown on the home page",
                          message_level="INFO")

        if self.use_option:
            if self.r1:
                self.r1.destroy()
            if self.r2:
                self.r2.destroy()

            self.r1 =self.tk.Label(self.root, text=f"{self.option_var.get()} selected!", foreground="blue")
            self.r1.place(x=298, y=480)


        if self.option_var.get() == "None" or self.option_var.get() == "add .ext":
            self.ext = None
        
        #########################

        elif self.option_var.get() != "add .ext":
            # if self.option_var.get()
            self.ext = self.option_var.get()

        elif self.text_ext == "add .ext" or not self.text_ext:
            self.ext = None

        elif self.text_ext:
            self.ext = self.text_ext

        self.use_option = True

# call function when we click on entry box
    def click(self, *args):
        logger.create_log(logger_name="home_page_ext.py", message="You clicked the extensions bar on the home page.", message_level="INFO")
        self.text_ext = self.search.get().strip(" ")
        if self.text_ext == 'add .ext':
            self.search.delete(0, 'end')
        self.root.focus()


# call function when we leave entry box
    def leave(self, *args):
        self.text_ext = self.search.get().strip(" ")
        logger.create_log(logger_name="main_directories.py", message="You hovered over the extensions bar on the home page.", message_level="INFO")
        self.text_ext = self.search.get().strip(" ")
        if self.text_ext == "":
            self.search.delete(0, 'end')
            self.search.insert(0, 'add .ext')
            self.root.focus()

# Call function, when pressed Enter key
    def callback(self, event):
        self.text_ext = self.search.get().strip(" ")
        logger.create_log(logger_name="home_page_ext.py", message=f"You entered ({self.text_ext}) extension in the main window extension bar.", message_level="INFO")

        if (self.text_ext=="add .ext" or not self.text_ext):
            if self.output_label:
                self.output_label.destroy()
            if self.r1:
                self.r1.destroy()
            if self.r2:
                self.r2.destroy()
            self.r2 = self.tk.Label(self.root, text=f"{self.text_ext}...Invalid Extension!", foreground="red")
            self.r2.place(x=298, y=480)

        else:
            if self.output_label:
                self.output_label.destroy()
            if self.r2:
                self.r2.destroy()
            if self.r1:
                self.r1.destroy()
            self.r1 = self.tk.Label(self.root, text=f"{self.text_ext} selected!", foreground="blue")
            self.r1.place(x=298, y=480)

            ########### PROCESS #############
            logger.create_log(logger_name="home_page_ext.py",
                              message=f"The extension {self.text_ext} is added to the list...",
                              message_level="INFO")

            self.use_option = False
            self.option_changed()
            self.create_wigets()

            ########### PROCESS END #########


if __name__ == "__main__":
    root = tk.Tk()
    SearchExt(root, tk, ttk)
    tk.mainloop()
