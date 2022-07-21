import pytest
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from pages.gshomepage import TestGSHomePage
from pages.itemscartpage import TestItemCart
from pages.produtpage import TestProductPage
from utilities.utils import Utils


@pytest.mark.usefixtures("GSSetup")
class TestGSshopnow:
    def testkardantnow(self):
        #Input Datas:
        kardantXpath = "//a[@href='https://gokaksweets.com/product/kardant/'][normalize-space()='Shop now']"
        kardantprice_1kg = "579.00"
        kardantprice_halfkg = "339.00"
        AddtoBasketXpath = "//button[normalize-space()='Add to basket']"
        weight = "//li[@title='1kg']"
        half_kg_weight = "//li[@title='500gm']"
        # Step1 : Connect to GS Sweets first: See conftest file
        # Check shop item (in our case Karadant)
        shopitem = TestGSHomePage(self.driver, self.wait)
        product_page = shopitem.test_shopitems(kardantXpath)
        # Product Page
        #Check Items Price Against test data
        product_page.test_itempricewithweights(kardantprice_halfkg, kardantprice_1kg )
        # Add Product to Cart scenario
        product_page.selectitems_weight(weight)
        user_cart = product_page.testadditemtobasket(AddtoBasketXpath)
        # Cart Page
        # Continue Shopping
        user_cart.continueshoping()
        product_page.selectitems_weight(half_kg_weight)
        product_page.testadditemtobasket(AddtoBasketXpath)
        time.sleep(2)
        Subtotal_new1 = user_cart.getItemcost()
        # SubTotal Verification against Items added to Cart
        SubTotalofEachItem = user_cart.getproductssubtotal()
        ut = Utils()
        ConvertedCurrency = ut.currencyConversion(SubTotalofEachItem)
        assert Subtotal_new1 == sum(ConvertedCurrency)
        #Applying Coupon and Total Verification and Test Cost After applying Coupon
        Total = user_cart.getTotalcost()
        couponcode = "2022RD5"
        FinalTotal = user_cart.testapplycoupon(couponcode,Total)
        if Total>= 999.00:
            assert FinalTotal == (Total - (Total * 0.05))
        else:
            assert FinalTotal == Total

