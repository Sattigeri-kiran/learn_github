import pytest
import time
from pages.gshomepage import TestGSHomePage
from ddt import ddt, data, unpack, file_data
import unittest
from utilities.utils import Utils


@pytest.mark.usefixtures("GSSetup")
@ddt
class TestReviewPage(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.home_page = TestGSHomePage(self.driver, self.wait)
        self.ut = Utils()

    #@file_data("../testdata/testdatayml.yaml")
    @data(*Utils.read_data_from_excel("D:\\WORK_WK\\learn_github\\testdata\\test.xlsx", "Sheet"))
    @unpack
    def test_reviewpagecheck(self, sort_by, sort_id):
        review_page = self.home_page.test_review_page()
        review_page.test_sort(sort_by, sort_id)
        time.sleep(2)
        # review_page.backtotop()
        review_count = review_page.loadmorereviews()
        assert review_count[0] > review_count[1], "Loaded Review count should be more"
        check_box = review_page.review_checkbox()
