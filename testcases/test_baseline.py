from utilities.ziputils import ZipUtils
from utilities.utils import Utils
import pytest
import unittest
from ddt import ddt, unpack, file_data, data

@ddt
class TestBaseline(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.zp = ZipUtils()

    #@data(*Utils.read_data_from_excel("testdatazipfile.xlsx", "Sheet1"))
    #@unpack
    @file_data("../testdata/testdatazipfile.json")
    def test_rebaseline(self, zip_filename):
        response = self.zp.extact_zipfile(zip_filename)
        assert len(response) == 1, "Some thing wrong with Extraction"
        rebaseline_response = self.zp.rebaseline(response[0])
        print(rebaseline_response)
        assert  rebaseline_response[0].endswith("deleteCitation.xml") == True, "Rebaseline output is not created Check"
        res = self.zp.create_zipfile(rebaseline_response[0])
        assert res == True , "Zip file is not created Check"
        check = self.zp.delete_downloaded_zipfile("./temp")
        assert len(check) == 0, "Temp file is not removed from temp location"




