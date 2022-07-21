import logging
import inspect


class Utils:
    def currencyConversion(self, list):
        Convertedlist = []
        for i in list:
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
