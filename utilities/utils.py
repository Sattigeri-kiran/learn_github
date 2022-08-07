import logging
import inspect
from openpyexcel import Workbook, load_workbook


class Utils:

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


