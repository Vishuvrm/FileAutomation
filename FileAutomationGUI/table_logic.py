from .logbase import logger
import os
import win32api
from .table import Table
import re
from .handling_zip import HandleZip

class SearchForFile:
    def __init__(self, extn, dir):
        self.extn = extn
        self.dir = dir
        self.table = None
        self.file_paths = []
        self.table_data = []
    def instance(self):
        return self


    def execute(self, file):
        drives = win32api.GetLogicalDriveStrings()
        drives = drives.split('\000')[:-1]

        lst = [[f"Sno.", "File name","File path"]]
        index = 1

        logger.create_log(logger_name="table_logic.py",
                          message=f"Your search for ({file}) for ({self.extn}) extension has following results:",
                          message_level="INFO")

        for drive in drives:
            renamed_file = None
            file_dir = None

            # Handling .zip files
            if file.endswith(".zip"):

                zip_handle = HandleZip(file, self.extn)
                lst = zip_handle.execute()

            else:
                # extn = self.extn
                if os.path.isdir(file):
                    drive = file
                    file_iterable = os.walk(drive)

                elif self.dir:
                    file_iterable = os.walk(self.dir)

                else:
                    file_iterable = os.walk(drive)



                # elif self.dir or file or self.extn:
                # elif file and not("." in file) and self.dir:
                #     file_iterable = os.walk(self.dir)
                #
                # elif file and re.search(f"[.]", file):
                #     extn = "."+file.split(".")[-1]
                #     # file = file.split(".")[0]
                #     if self.dir:
                #         file_iterable = os.walk(self.dir)
                #
                #
                #
                # elif file and self.extn:
                #     extn = self.extn
                #
                # elif self.extn and self.dir:
                #     extn = self.extn
                #     file_iterable = os.walk(self.dir)
                # elif self.extn:
                #     extn = self.extn
                # elif self.dir:
                #     file_iterable = os.walk(self.dir)
                #
                # else:
                #     file_iterable = os.walk(drive)
                #
                # if not self.extn:
                #     self.extn = extn


                for dirpath, dirnames, filenames in file_iterable:
                    if drive == file:
                        file_dir = file

                    for filename in filenames:
                        # When entry given is a directory path
                        if file_dir:
                            if self.extn:
                                if self.extn == "png/jpg":
                                    if filename.endswith(".png") or filename.endswith(".jpg"):
                                        renamed_file = filename
                                elif filename.endswith(self.extn):
                                    renamed_file = filename

                            else:
                                renamed_file = filename


                        #  When no entry is given
                        elif file:
                            if self.extn:
                                if self.extn == "png/jpg":
                                    if filename.endswith(".png") or filename.endswith(".jpg"):
                                        renamed_file = filename

                                elif filename.endswith(self.extn) and (file in filename):
                                    renamed_file = filename

                            else:
                                if file in filename:
                                    if re.search(r"\.\w+$",file):
                                        renamed_file = file

                                    elif self.extn:
                                        if self.extn == "png/jpg":
                                            if filename.endswith(".png") or filename.endswith(".jpg"):
                                                renamed_file = filename
                                        elif filename.endswith(self.extn):
                                            renamed_file = filename

                                    else:
                                        renamed_file = filename



                                elif file.startswith("."):
                                    if not self.extn:
                                        self.extn = re.findall(r"[^.]\w+", file)[-1]
                                        print("=>",self.extn)

                                    elif self.extn:
                                        if self.extn == "png/jpg":
                                            if filename.endswith(".png") or filename.endswith(".jpg"):
                                                renamed_file = filename
                                        elif filename.endswith(self.extn):
                                            renamed_file = filename



                                elif file.lower() in filename.lower():
                                    if not self.extn:
                                        try:
                                            self.extn = re.findall(r"[^.]\w+", file)[-1]
                                            if filename.endswith(self.extn):
                                                renamed_file = filename
                                        except:
                                            renamed_file = filename
                                    elif self.extn:
                                        if self.extn == "png/jpg":
                                            if filename.endswith(".png") or filename.endswith(".jpg"):
                                                renamed_file = filename

                                        elif filename.endswith(self.extn):
                                            renamed_file = filename
                        else:
                            if self.extn:
                                if self.extn == "png/jpg":
                                    if filename.endswith(".png") or filename.endswith(".jpg"):
                                        renamed_file = filename

                                elif filename.endswith(self.extn):
                                    renamed_file = filename
                            else:
                                renamed_file = filename


                        if renamed_file==filename:
                            logger.create_log(logger_name="table_logic.py",
                                              message=f"file#{index}: {dirpath}\\{renamed_file}",
                                              message_level="INFO")
                            file_path = os.path.join(dirpath, renamed_file)
                            self.file_paths.append(file_path)
                            lst.append((index, renamed_file, file_path))
                            lst[0][0] = f"Sno.({index})"
                            index += 1
                if file_dir:
                    logger.create_log(logger_name="table_logic.py",
                                      message=f"Your search for ({file}) for ({self.extn}) extension has completed!",
                                      message_level="INFO")
                    break

                if self.dir:
                    break

                logger.create_log(logger_name="table_logic.py",
                                  message=f"Your search for ({file}) for ({self.extn}) extension has completed!",
                                  message_level="INFO")

        # # Create the table for the list created.
        self.table_data = lst
        self.table = Table(self.file_paths)
        if len(self.table_data)!=1:
            self.process = self.table.execute(self.table_data, file)
        else:
            self.table_data.append(("None","None","None","None"))
            self.process = self.table.execute(self.table_data, file)



    def quit_window(self):
        self.table.destroy()

    def renew(self):
        self.file_paths = []






