import unittest
import pytest
from pages.gshomepage import TestGSHomePage
from ddt import ddt, file_data


@pytest.mark.usefixtures("GSSetup")
@ddt
class TestContactus(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.home_page = TestGSHomePage(self.driver, self.wait)

    @file_data("../testdata/testcontactusdata.json")
    def test_emailId(self, emailId, message):
        contactus_page = self.home_page.test_contactuspage()
        assert_message = contactus_page.test_email(emailId)
        assert assert_message == message

    def test_contactus_fields(self):
        contactus_page = self.home_page.test_contactuspage()
        contactus_page.test_contact_us()

