from .logbase import logger

from tkinter import *
import tkinter as tk
from tkinter import ttk
# pip install pillow => Python Imaging Library
# from PIL import Image, ImageTk
from .table_logic import SearchForFile
from .home_page_ext import SearchExt
from .main_directories import GetDirectories


class Application:
    def __init__(self, logger):
        self.logger = logger
        self.root = Tk()
        # Let's set the basic layout features of the GUI window
        # root.geometry("733x434")
        self.root.minsize(800, 600)
        self.root.title("FileAutomation")

        # Some flags
        self.r1 = None
        self.r2 = None

        self.basic_buildup()

###### PART1(PART2) #####
# call function when we click on entry box
    def click(self, *args):
        self.logger.create_log(logger_name="app.py", message="You clicked the search bar on the home page.", message_level="INFO")
        if self.search.get() == 'Search for the file(With Extension)':
            self.search.delete(0, 'end')
        self.root.focus()


# call function when we leave entry box
    def leave(self, *args):
        self.logger.create_log(logger_name="app.py", message="You hovered over the search bar on the main window.", message_level="INFO")

        if self.search.get() == "":
            self.search.delete(0, 'end')
            self.search.insert(0, 'Search for the file(With Extension)')
            self.root.focus()

# Call function, when pressed Enter key

    def callback(self, event):
        self.logger.create_log(logger_name="app.py", message=f"You searched for ({self.file.get()}) for ({self.extension.ext}) extension in the main window search bar.", message_level="INFO")
        try:
            if self.search_window:
                self.search_window.quit_window()
        except Exception:
            self.logger.create_log(logger_name="app.py",
                                   message=f"You closed the Window!",
                                   message_level="INFO")

        self.extn = self.extension.ext
        self.dir = self.directory.dir

        if self.file.get() == "":
            filename = "All"
            if self.extn:
                ext = self.extn
            else:
                ext = ""
        elif not self.extn or self.file.get():
            ext = ""
            filename = self.file.get()
        else:
            filename = self.file.get()
            ext = self.ext

        if self.r1:
            self.r1.destroy()

        if self.r2:
            self.r2.destroy()

        if (self.search.get()=='Search for the file' or self.search.get()=="") and not self.extn and not self.dir:
            self.r2 = Label(self.frame2, text="Input the file name!", foreground="red")
            self.r2.pack()
            if self.r1:
                self.r1.destroy()

        else:
            self.r1 = Label(self.root, text=f"See the results for ({self.dir}...{filename}{ext}) in the new window.")
            self.r1.pack(side=BOTTOM)
            if self.r2:
                self.r2.destroy()

            ########### PROCESS #############
            self.logger.create_log(logger_name="app.py",
                              message=f"The process of search for ({self.file.get()}) for ({self.extension.ext}) extension has started!",
                              message_level="INFO")

            # Creates new instance each time
            self.search_window = SearchForFile(self.extn, self.dir).instance()
            self.search_window.execute(self.file.get())

            # Renew it's data as well
            ########### PROCESS END #########




    def basic_buildup(self):
        ################# TOP FRAME ###############################
        self.frame_top = Frame(self.root)
        self.frame_top.pack(side=TOP, fill=X)
        self.text_label1 = Label(self.frame_top, text="Welcome to FileAutomation",
                                 font=("comicsense", 15, "bold"),
                                 pady=5,
                                 relief="groove"
                                 )
        self.text_label1.pack(fill=X)
        ##################### MIDDLE PART ###########################

        ###### PART1 ############
        self.frame1 = Frame(self.root)
        # Let's add image to the GUI window
        # self.photo = PhotoImage(file="E:\\iNeuronProject\\FileAutomationGUI\\automation-diagram.png")
        self.photo = PhotoImage(file="F:\iNeuronProject\App_Exe\FileAutomationGUI\\automation-diagram.png")

        self.img_label = Label(self.frame1, image=self.photo)
        self.img_label.pack()
        self.frame1.pack()

        self.file = StringVar()

        self.frame2 = Frame(self.frame1)
        self.frame2.pack(side=BOTTOM, fill=tk.X, expand=True)

        self.search = Entry(self.frame2, text="Search", bd=5, font="Calibri 10", width=60, textvariable=self.file)


        # Add text in Entry box
        self.search.insert(0, "Search for the file(With Extension)")

        # Create Extensions widgets
        self.extension = SearchExt(self.frame2, self.root, tk, ttk)
        # Adding Directories widget
        self.directory = GetDirectories(self.root, tk, ttk)

        # Use bind method
        self.search.bind("<Button-1>", self.click) # Left click
        self.search.bind("<Leave>", self.leave)

        # self.r1 = Label(self.frame2)
        # self.r1.pack()
        # self.r2 = Label(self.frame2)
        # self.r2.pack()
        self.search_window = None
        self.search.bind('<Return>', self.callback)

        self.search.pack(expand = True)
##################### MIDDLE PART END #######################

################# BOTTOM FRAME ############################
        self.frame_bottom = Frame(self.root, background="green", relief=GROOVE)
        self.frame_bottom.pack(side=BOTTOM, fill=X)
        self.textlabel2 = Label(self.frame_bottom, text="application is ready!",
                              foreground="white",
                              background="green")
        self.textlabel2.pack()

        self.root.mainloop()