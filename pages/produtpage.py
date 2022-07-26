import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
from pages.itemscartpage import TestItemCart
from utilities.utils import Utils


class TestProductPage:
    log = Utils.custlogger(logLevel=logging.WARNING)

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    def test_itempricewithweights(self, halfkg_price, kg_price, item):
        rs = u"\u20B9"
        price_XPath = "//ins//bdi[1]"
        Weight_XPath = "//li[@title='1kg']"
        Clear_XPath = "//a[normalize-space()='Clear']"
        AddToBasket_XPath = "//button[normalize-space()='Add to basket']"

        # Half KG Price Verification
        value_halfkg = self.wait.until(EC.presence_of_element_located((By.XPATH, price_XPath)))
        rupee = str(rs) + halfkg_price
        assert value_halfkg.text == rupee, "Half KG " + item + "Price should be" + halfkg_price
        # One KG Price Verification
        element = self.wait.until(EC.element_to_be_clickable((By.XPATH, Weight_XPath)))
        element.click()
        value_kg = self.wait.until(EC.presence_of_element_located((By.XPATH, price_XPath)))
        assert value_kg.text == str(rs) + kg_price, "One KG " + item + " Price should be " + kg_price
        self.log.info("Checked the Items cost based on weight")
        self.driver.find_element(By.XPATH, Clear_XPath).click()
        self.log.warning("Cleared" + item + "Price tag")
        value_default = self.wait.until(EC.presence_of_element_located((By.XPATH, price_XPath)))
        time.sleep(2)
        assert value_default.text == ""
        # Add to Basket Verification without selecting items
        self.driver.find_element(By.XPATH, AddToBasket_XPath).click()
        self.driver.switch_to.alert.accept()
        self.log.warning("Please select some product options before adding this product to your basket.")

    def selectitems_weight(self, weight):
        element = self.wait.until(EC.element_to_be_clickable((By.XPATH, weight)))
        element.click()
        self.log.info(weight + " Is selected from Product Page")

    def testadditemtobasket(self, locator):
        element = self.wait.until(EC.element_to_be_clickable((By.XPATH, locator)))
        element.click()
        user_cart = TestItemCart(self.driver, self.wait)
        self.log.info("In Item Cart Page")
        return user_cart
