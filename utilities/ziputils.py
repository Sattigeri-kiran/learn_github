import logging
import os
from zipfile import ZipFile
from utilities.utils import Utils
import xml.etree.ElementTree as ET


class ZipUtils:
    log = Utils.custlogger(logLevel=logging.DEBUG)

    def extact_zipfile(self, file_name):
        print("filename", file_name, os.getcwd())

        with ZipFile("./testdata/testdatafiles/" + file_name) as e_zipfile:
            e_zipfile.extractall("./temp")
            data = e_zipfile.namelist()
            self.log.info("Extracted Zip file sent to Re baseline")
        return data

    def rebaseline(self, file):
        real_file_name = file.split(".")
        root_node = ET.parse("./temp/" + file)
        myroot = root_node.getroot()
        ch = myroot.findall('PubmedArticle')
        for item in ch:
            myroot.remove(item)
        root_node.write("./temp/" + real_file_name[0] + ".deleteCitation.xml", encoding="UTF-8", xml_declaration=True)
        self.log.info("Re baseline is Completed")
        return os.listdir("./temp")

    def create_zipfile(self, deleteCitation_file):
        output_file_name = deleteCitation_file.split(".")
        with ZipFile("./output/" + output_file_name[0] + ".deleteCitation.zip", 'w') as w_zipfile:
            os.chdir("./temp")
            w_zipfile.write(deleteCitation_file)
            self.log.info("Created the NewZip file")
            os.chdir("../")
            print("./output/" + output_file_name[0] + ".deleteCitation.zip")
            return os.path.exists("./output/" + output_file_name[0] + ".deleteCitation.zip")

    def delete_downloaded_zipfile(self, dir):
        for temp_file in os.listdir(dir):
            os.remove(os.path.join(dir, temp_file))
        self.log.warning("Deleted the File Successfully from temp location")
        check = os.listdir(dir)
        return check
