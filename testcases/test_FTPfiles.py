import re
import pytest
from utilities.utils import Utils


@pytest.mark.usefixtures("FTPsetup")
class TestFTPConnection:
    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.ut = Utils(self.ftp)

    def test_ftp_connection(self):
        file_name = "test-file.zip"
        output = self.ut.uploadfiles_to_ftp(file_name)
        for item in output:
            if item == "test-file.zip":
                file = True
            else:
                file = False
        assert file == True, "Uploaded file should present"
        downloaded_file = self.ut.downloadfiles_from_ftp(file_name)
        assert downloaded_file[1] == True, "Downloaded file should present in output location"
        file = self.ut.read_downloaded_zipfile("mock-test-file.xml", downloaded_file[0])
        testmrid = re.findall("<tstmrid>(.*?)</tstmrid>", file)
        assert len(testmrid) == 2, "length of tstmrid should be 2"




        '''
        ftp = FTP("ftp.dlptest.com")
        ftp.login("dlpuser", 'rNrKYTX9g7z3RgJRmxWuGHbeu')
        #FTP.getwelcome(self)
        # print(ftp.mkd("/test-dir"))
        ftp.cwd("/test-dir")
        file_name = "test-file.zip"
        with open("D:/out.4372347846701421776/test-file.zip", "rb") as my_file:
            ftp.storbinary(f"STOR {file_name}", my_file)
        print(ftp.dir())
        ftp.quit() 
        def test_ftpdownload(self):
        file_name = "output-test-file.zip"
        with open(file_name, "wb") as file:
            self.ftp.retrbinary(f"RETR {file_name}", file.write)

        def test_ftpread(self):
        file_name = "test-file.zip"
        with ZipFile(file_name) as zip_file:
            output = zip_file.read("asset_00001.xml")
            print(str(output))
        '''
