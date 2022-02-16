# Python program to create a table
from .logbase import logger

from tkinter import *
from tkinter import ttk
import tkinter.scrolledtext as scrolledtext
from .extensions import App

class Table:
    def __init__(self, file_paths):
        self.root = Tk()
        self.root.maxsize(1500,500)
        self.e = None
        self.app = None
        self.table_data = None

        self.button_frame = Frame(self.root)
        self.button_frame.pack(side=TOP)

        self.frame1 = Frame(self.root)
        self.frame1.pack()

        self.textbox = scrolledtext.ScrolledText(self.root, undo=True)
        self.textbox.pack(expand=True, fill='both', pady=50)

        self.file_paths = file_paths

    def instance(self):
        return self

    def execute(self, lst, file):

        self.table_data = lst
        self.root.title(f"Search results for the ({file})")
        self.merge = Button(self.button_frame,text="Merge all!", command=self.extension).pack(pady=10)



        # code for creating table
        # find total number of rows and
        # columns in list
        total_rows = len(lst)
        total_columns = len(lst[0])
        # Maximum width for each column:
        max_width = {}
        for j in range(total_columns):
            for i in range(total_rows):
                if j in max_width:
                    if max_width[j] < len(str(lst[i][j])):
                        max_width[j] = len(str(lst[i][j]))
                else:
                    max_width[j] = len(str(lst[i][j]))

        for i in range(total_rows):
            if self.character_limit(i):
                for j in range(total_columns):
                    if max_width[j]>50:
                        max_width[j] = 50

                    self.e = Entry(self.textbox, width=max_width[j], fg='blue',
                                   font=('Arial', 16, 'bold'))

                    self.e.grid(row=i, column=j)
                    self.e.insert(END, lst[i][j])

                    self.e["state"]="readonly"


        self.e.grid()

        mainloop()

    def character_limit(self, rowno,  maxrows=100):
        if rowno > maxrows:
            return False
        else:
            return True

    def destroy(self, *addons):
        self.root.destroy()
        if self.app:
            self.app.destroy()

    def extension(self):
        logger.create_log(logger_name="table.py",
                          message="You clicked the Merge all! button on the top.",
                          message_level="INFO")
        if self.app:
            self.app.destroy()
        self.app = App(self.file_paths)
        self.app.mainloop()










