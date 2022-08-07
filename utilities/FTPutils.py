import logging
import os
from zipfile import ZipFile
from utilities.utils import Utils


class FTPUtils:
    log = Utils.custlogger(logLevel=logging.INFO)

    def __init__(self, ftp):
        self.ftp = ftp

    def uploadfiles_to_ftp(self, file_name):
        with open("./testdata/" + file_name, "rb") as my_file:
            self.ftp.storbinary(f"STOR {file_name}", my_file)
        self.log.info("Uploaded files to FTP location")
        return self.ftp.nlst()

    def downloadfiles_from_ftp(self, file_name):
        with open("./output/" + file_name, "wb") as file:
            self.ftp.retrbinary(f"RETR {file_name}", file.write)
        self.log.info("Downloaded files from FTP")
        return ["./output/" + file_name, os.path.exists("./output/" + file_name)]

    def read_downloaded_zipfile(self, file_name, file_location):
        with ZipFile(file_location) as my_zip_file:
            output = my_zip_file.read(file_name)
        self.log.info("Reading the Zipped file from Local")
        return str(output)


