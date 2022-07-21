from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

from pages.itemscartpage import TestItemCart


class TestProductPage:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    def test_itempricewithweights(self, halfkg_price, kg_price):
        value_halfkg = self.driver.find_element(By.XPATH, "//ins//bdi[1]")
        rs = u"\u20B9"
        rupee = str(rs) + halfkg_price
        assert value_halfkg.text == rupee
        element = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//li[@title='1kg']")))
        element.click()
        value_kg = self.driver.find_element(By.XPATH, "//ins//bdi[1]")
        assert value_kg.text == str(rs) + kg_price
        self.driver.find_element(By.XPATH, "//a[normalize-space()='Clear']").click()
        value_default = self.wait.until(EC.presence_of_element_located((By.XPATH, "//ins//bdi[1]")))
        time.sleep(2)
        assert value_default.text == ""
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Add to basket']").click()
        self.driver.switch_to.alert.accept()

    def selectitems_weight(self, weight):
        element = self.wait.until(EC.element_to_be_clickable((By.XPATH, weight)))
        element.click()

    def testadditemtobasket(self, locator):
        element = self.wait.until(EC.element_to_be_clickable((By.XPATH, locator)))
        element.click()
        user_cart = TestItemCart(self.driver, self.wait)
        return user_cart
