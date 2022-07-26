import pytest
from pages.gshomepage import TestGSHomePage
from utilities.utils import Utils
import unittest
from ddt import file_data, ddt
from selenium.webdriver.common.by import By
import time

@pytest.mark.usefixtures("GSSetup")
@ddt
class TestGSshopnow(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def class_setup(self):
        # Step1 : Connect to GS Sweets first: See conftest file
        self.shop_item = TestGSHomePage(self.driver, self.wait)
        self.ut = Utils()

    @file_data("../testdata/testItemsdata.json")
    def test_gsitem_price(self, item_Xpath, item_price_halfkg, item_price_1kg, item):
        # Test the Item Price based on weight
        product_page = self.shop_item.test_shopitems(item_Xpath)
        product_page.test_itempricewithweights(item_price_halfkg, item_price_1kg, item)
        self.driver.find_element(By.ID, "menu-item-1144").click()
        '''
        # Applying Coupon and Total Verification and Test Cost After applying Coupon
        Total = user_cart.getTotalcost()
        couponcode = "2022RD5"
        FinalTotal = user_cart.testapplycoupon(couponcode, Total)
        if Total >= 999.00:
            assert FinalTotal == (Total - (Total * 0.05))
        else:
            assert FinalTotal == Total
            '''
