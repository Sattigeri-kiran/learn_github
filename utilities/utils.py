import logging
import inspect
from os import path
from zipfile import ZipFile
from openpyexcel import Workbook, load_workbook


class Utils:

    def __init__(self, ftp):
        self.ftp = ftp

    def currencyConversion(self, list1):
        Convertedlist = []
        for i in list1:
            Convertedlist.append(float(i.replace('\u20B9', '')))
        return Convertedlist

    def custlogger(logLevel=logging.DEBUG):
        # set class/method name from where it is called
        logger_name = inspect.stack()[1][3]
        # create logger
        logger = logging.getLogger(logger_name)
        logger.setLevel(logLevel)
        # create console handler
        fh = logging.FileHandler("automation.log")
        ch = logging.StreamHandler()
        # create formatter
        formatter = logging.Formatter('%(asctime)s -%(levelname)s-%(name)s:%(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        # add formatter to console or file handler
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)
        # add console handler to logger
        logger.addHandler(fh)
        logger.addHandler(ch)
        return logger

    def read_data_from_excel(self, file_name, sheet):
        data_list = []
        wb = load_workbook(filename=file_name)
        sh = wb[sheet]
        row_ct = sh.max_row
        col_ct = sh.max_column

        for i in range(2, row_ct + 1):
            row = []
            for j in range(1, col_ct + 1):
                row.append(sh.cell(row=i, column=j).value)
            data_list.append(row)
        return data_list

    def uploadfiles_to_ftp(self, file_name):
        with open("./testdata/" + file_name, "rb") as my_file:
            self.ftp.storbinary(f"STOR {file_name}", my_file)
        return self.ftp.nlst()

    def downloadfiles_from_ftp(self, file_name):
        with open("./output/" + file_name, "wb") as file:
            self.ftp.retrbinary(f"RETR {file_name}", file.write)
        return ["./output/" + file_name, path.exists("./output/" + file_name)]

    def read_downloaded_zipfile(self, file_name, file_location):
        with ZipFile(file_location) as my_zip_file:
            output = my_zip_file.read(file_name)
            return str(output)
