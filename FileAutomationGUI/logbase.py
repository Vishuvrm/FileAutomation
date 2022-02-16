import logging
import os
import re

logging.basicConfig()

class LogBase:
    def __init__(self, dir_name = None, logger_name = __name__, create_new_file=True):
        self.latest_file = None
        self.dir_name = dir_name
        self.logger_name = logger_name
        self.logger_name_list = set()
        self.create_new_file = create_new_file

        self.file_logger = None
        self.console_logger = None


    def create_log(self, filename=None, logger_name:"Root logger name" = None, message=None,
                     message_level:"DEBUG INFO WARNING ERROR CRITICAL" = None,  level=logging.DEBUG,
                   mode = "a",  style = "{",
                   format = "{name}:: (Time: {asctime}) --|--> {levelname} --|--> '{message}'" ):

        if not logger_name:
            logger_name = self.logger_name


        if self.dir_name:
            if not os.path.exists(self.dir_name):
                self.create_directory(self.dir_name)

            if self.create_new_file:
                file_no = self.get_logfile_no(filename)
                if filename:
                    self.latest_file  = f"{filename}_{file_no}.log"
                else:
                    self.latest_file =f"log_{file_no}.log"

        self.create_new_file = False

        self.write_to_log(filename, logger_name, message, message_level, level, mode, style, format)



    def write_to_log(self, filename, logger_name, message, message_level, level, mode,  style, format):

        if self.dir_name:
            if not filename:
                filename = self.latest_file
            else:
                pass
            filename = os.path.join(self.dir_name, filename)
            if logger_name not in self.logger_name_list:
                self.file_logger = self.get_logger_for_file(logger_name, filename,mode, style, format, level )
                self.logger_name_list.add(logger_name)

            if message_level == "DEBUG":
                self.file_logger.debug(message)
            elif message_level == "INFO":
                self.file_logger.info(message)
            elif message_level == "WARNING":
                self.file_logger.warning(message)
            elif message_level == "ERROR":
                self.file_logger.error(message)
            elif message_level == "CRITICAL":
                self.file_logger.critical(message)
            elif message_level == "EXCEPTION":
                self.file_logger.exception(message)

        elif not self.dir_name:
            if logger_name not in self.logger_name_list:
                self.console_logger = self.get_logger_for_console(level, logger_name, style, format)
                self.logger_name_list.add(logger_name)

            if message_level == "DEBUG":
                self.console_logger.debug(message)
            elif message_level == "INFO":
                self.console_logger.info(message)
            elif message_level == "WARNING":
                self.console_logger.warning(message)
            elif message_level == "ERROR":
                self.console_logger.error(message)
            elif message_level == "CRITICAL":
                self.console_logger.critical(message)
            elif message_level == "EXCEPTION":
                self.console_logger.exception(message)


    def file_handler(self, file_name, style,  fmt_file, mode):
        FORMATTER = logging.Formatter(fmt_file, style=style)
        file = logging.FileHandler(file_name, mode=mode)
        file.setFormatter(FORMATTER)
        return file

    def console_handler(self, style, format):
        FORMATTER = logging.Formatter(style = style, fmt = format)
        console_hndlr = logging.StreamHandler()
        console_hndlr.setFormatter(FORMATTER)
        return console_hndlr

    def get_logger_for_file(self, logger_name, file_name, file_mode, style, fmt_file, level=logging.DEBUG):
        logger = logging.getLogger(logger_name)
        logger.addHandler(self.file_handler(file_name, style, fmt_file, file_mode))
        logger.setLevel(level)
        return logger

    def get_logger_for_console(self, level, logger_name, style, format):
        logger = logging.getLogger(logger_name)
        logger.addHandler(self.console_handler(style, format))
        logger.setLevel(level)
        return logger


    def numeric_index(self, file):
        search_num = re.search(r"\d+", file)
        return search_num

    def sort_log_files(self, log_files):
        return sorted(log_files, key=lambda x: int(x[self.numeric_index(x).start(): self.numeric_index(x).end()]))

    def create_directory(self, dir_name):

        # Create a logging direcory
        try:
            if not os.path.isdir(dir_name):
                os.mkdir(dir_name)
        except FileExistsError as e:
            print(e)


    def get_logfile_no(self, filename = None):

        log_files = os.listdir(self.dir_name)

        # Create the log file

        if not log_files:
            file_no = 1

        else:
            log_files = self.sort_log_files(log_files)
            self.latest_file = log_files[-1]
            file_no = int(re.findall(r"\d+", self.latest_file)[0]) + 1
        return file_no



    def shutdown(self):
        logging.shutdown()



if __name__ != "__main__":
    logger = LogBase("Logger")

