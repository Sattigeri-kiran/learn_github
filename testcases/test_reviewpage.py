import pytest
import time
from pages.gshomepage import TestGSHomePage


@pytest.mark.usefixtures("GSSetup")
class TestReviewPage:
    def class_setup(self):
        self.o_page = TestGSHomePage(self.driver, self.wait)

    def test_reviewpage(self):
        review_page = self.o_page.test_review_page()
        review_page.test_sort(2, "wc-block-components-sort-select__select-0")
        time.sleep(5)
        # review_page.backtotop()
        review_count = review_page.loadmorereviews()
        assert review_count[0] > review_count[1], "Loaded Review count should be more"
        check_box = review_page.review_checkbox()
        time.sleep(6)
        print(check_box)
