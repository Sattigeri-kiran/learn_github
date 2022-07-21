import pytest
import time
from pages.gshomepage import TestGSHomePage
from pages.itemscartpage import TestItemCart
from pages.produtpage import TestProductPage


@pytest.mark.usefixtures("GSSetup")
class TestGSshopladu:
    def testladdunow(self):
        # Values
        laddu = "//a[@href='https://gokaksweets.com/product/special-ladagi-laddu/'][normalize-space()='Shop now']"
        laddu_prices = ["229.00", "349.00"]
        laddu_weights = ["//li[@title='1kg']", "//li[@title='500gm']"]
        addtobasket = "//button[normalize-space()='Add to basket']"
        productname = "Ladagi laddu - 1kg"
        productqty = '1'
        couponcode = "2022RD5"

        # Shop Ladagi Laddu
        laddushop = TestGSHomePage(self.driver, self.wait)
        product_page = laddushop.test_shopitems(laddu)
        product_page.test_itempricewithweights(laddu_prices[0], laddu_prices[1])
        product_page.selectitems_weight(laddu_weights[0])
        user_cart = product_page.testadditemtobasket(addtobasket)
        user_cart.AddItemQty(productname, productqty)
        time.sleep(3)
        Total = user_cart.getTotalcost()
        print("The Total", Total)
        FinalTotal = user_cart.testapplycoupon(couponcode, Total)
        if Total >= 999.00:
            assert FinalTotal == (Total - (Total * 0.05))
        else:
            assert FinalTotal == Total
