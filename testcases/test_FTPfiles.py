import re
import pytest
from utilities.FTPutils import FTPUtils


@pytest.mark.usefixtures("FTPsetup")
class TestFTPConnection:
    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.ut = FTPUtils(self.ftp)

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
        check = self.ut.delete_downloaded_zipfile(downloaded_file[0])
        assert len(check) == 0, "File is not deleted form output location check"
