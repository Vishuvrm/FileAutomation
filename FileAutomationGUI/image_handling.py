from .logbase import logger
import math
from PIL import Image

class ImageHandler:

    def __init__(self):
        self.wrong_files = 0
        self.correct_files = 0

    def __optimum_cols(self, n):
        for i in range(n, n ** 2 + 1):
            sqrt = math.sqrt(i)
            if int(sqrt) * int(sqrt) == (i):
                return int(sqrt)


    def merge_img(self, *files, size=(200, 200), max_img_in_col=None, save_as=None, extn):
        total_imgs = len(files)


        if not max_img_in_col:
            max_img_in_col = self.__optimum_cols(total_imgs)

        for file in files:
            try:
                img = Image.open(file).resize(size)
            except Exception as e:
                pass
        total_width = max_img_in_col * size[0]
        total_height = math.ceil(total_imgs / max_img_in_col) * size[1]
        if extn == ".png":
            mode = "RGBA"
        elif extn == ".jpg":
            mode = "RGB"
        new_img = Image.new(mode, size=(total_width, total_height))

        left, i = 0, 0
        top, j = 0, 0


        for file in files:
            try:
                img = Image.open(file).resize(size)
                img_width = img.size[0]
                img_height = img.size[1]

                if i == max_img_in_col:
                    top += img_height
                    left, i = 0, 0

                new_img.paste(img, (left, top))

                if i < max_img_in_col:
                    left += img_width
                    i += 1

                self.correct_files += 1
            except Exception as e:
                logger.create_log(logger_name="image_handling.py", message=f"FAILED!! : {file}",
                                  message_level="ERROR")
                logger.create_log(logger_name="image_handling.py", message=e, message_level="EXCEPTION")
                self.wrong_files += 1
                continue

        if save_as:
            new_img.save(save_as)

        return new_img