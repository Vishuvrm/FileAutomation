from zipfile import ZipFile
import os
import re

class HandleZip:
    def __init__(self, zfile, extn = None):
        self.zfile = zfile
        self.extn = extn
        self.lst_of_files = None
        self.lst_of_paths = None
        self.lst_of_dir = None

        self.get_files()
        self.get_file_paths()
        self.get_directory()

        self.file_iterable = zip(self.lst_of_paths, self.lst_of_dir, self.lst_of_files)

    def get_files(self):
        with ZipFile(self.zfile, 'r') as zipObj:
            # Get list of files names in zip
            listOfiles = zipObj.namelist()
            # Iterate over the list of file names in given list & print them

            self.lst_of_files = listOfiles

    def get_file_paths(self):
        self.lst_of_paths = [os.path.join(self.zfile, file) for file in self.lst_of_files]

    def get_directory(self):
        main_dir = re.findall(r"[^\\^/]{1,2}\w+\.zip$", self.zfile)[-1]
        self.lst_of_dir = [path.split(main_dir+"\\")[-1] for path in self.lst_of_paths]

    def execute(self):
        lst = [[f"Sno.", "File name", "File path"]]
        index = 1

        for dirpath, dirname, filename in self.file_iterable:
            if self.extn:
                if filename.endswith(self.extn):
                    file = filename
                else:
                    file = filename
            else:
                file = filename

            if filename == file:
                lst.append((index, file, dirpath))
                lst[0][0] = f"Sno.({index})"
                index += 1

        return lst


if __name__ == "__main__":
    filez = "C:\\Users\\vishu\\Downloads\\Automate_the_Boring_Stuff_2e_onlinematerials.zip"
    listzip = HandleZip(filez, "py")
    listzip.execute()