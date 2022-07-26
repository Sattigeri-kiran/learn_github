import time
import unittest
import pytest
from selenium.webdriver.common.by import By
from pages.gshomepage import TestGSHomePage
from utilities.utils import Utils
from ddt import ddt, file_data


@pytest.mark.usefixtures("GSSetup")
@ddt
class TestItemCartcost(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.shop_item_cart = TestGSHomePage(self.driver, self.wait)
        self.ut = Utils()

    @file_data("../testdata/testItemcartcost.json")
    def test_cart_cost(self, item_Xpath, AddtoBasketXpath, weight, half_kg_weight):
        product_item_page = self.shop_item_cart.test_shopitems(item_Xpath)
        product_item_page.selectitems_weight(weight)
        user_cart = product_item_page.testadditemtobasket(AddtoBasketXpath)
        # Cart Page and Continue Shopping
        time.sleep(2)
        user_cart.continueshoping()
        product_item_page.selectitems_weight(half_kg_weight)
        product_item_page.testadditemtobasket(AddtoBasketXpath)
        Subtotal_new1 = user_cart.getItemcost()
        # SubTotal Verification against Items added to Cart
        sub_total_of_each_item = user_cart.getproductssubtotal()
        ConvertedCurrency = self.ut.currencyConversion(sub_total_of_each_item)
        assert Subtotal_new1 == sum(ConvertedCurrency)
        self.driver.find_element(By.ID, "menu-item-1144").click()
