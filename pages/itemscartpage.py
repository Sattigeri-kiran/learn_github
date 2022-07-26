import logging
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from utilities.utils import Utils


class TestItemCart:
    log = Utils.custlogger(logLevel=logging.WARNING)

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    def AddItemQty(self, productname, productqty):

        product_quantity_XPath = "//td[@class='product-quantity']//div//input"
        product_name_XPath = "//td[@class='product-name']//a"
        update_basket = "//button[normalize-space()='Update basket']"

        CartProducts = self.driver.find_elements(By.XPATH, product_quantity_XPath)
        for i in CartProducts:
            product = self.driver.find_elements(By.XPATH, product_name_XPath)
            if product[0].text == productname:
                i.clear()
                i.send_keys(productqty)
            else:
                i.clear()
                i.send_keys(productqty)
            time.sleep(5)
            self.log.info("Added the Product Quantity")
        element = self.wait.until(EC.element_to_be_clickable((By.XPATH, update_basket)))
        element.click()
        self.log.warning("Updated the Product Basket")

    def getItemcost(self):
        cart_subtotal_XPath = "//tr[@class='cart-subtotal']//bdi[1]"
        Subtotal = self.wait.until(EC.presence_of_element_located((By.XPATH, cart_subtotal_XPath)))
        Subtotal_new = self.driver.find_element(By.XPATH, cart_subtotal_XPath)
        Conv1 = Subtotal.text.replace('\u20B9', '')
        Subtotal_new1 = float(Conv1.replace(',', ''))
        self.log.info("Getting Product SubTotal ")
        return Subtotal_new1

    def getTotalcost(self):
        self.log.info("Getting Product Total - Started")
        cart_total_XPath = "//tr[@class='order-total']//bdi[1]"
        total_items_value = self.wait.until(EC.presence_of_element_located((By.XPATH, cart_total_XPath)))
        Conversion = total_items_value.text.replace('\u20B9', '')
        Total = float(Conversion.replace(',', ''))
        self.log.info("Getting Product Total - Completed")
        return Total

    def testapplycoupon(self, coupon_code, total):
        if total >= 999.00:
            time.sleep(4)
            self.driver.find_element(By.XPATH, "//input[@id='coupon_code']").send_keys(coupon_code)
            time.sleep(3)
            self.driver.find_element(By.XPATH, "//button[normalize-space()='Apply coupon']").click()
            time.sleep(3)
            finalitemvalue = self.driver.find_element(By.XPATH, "//tr[@class='order-total']//bdi[1]")
            Conv = finalitemvalue.text.replace('\u20B9', '')
            FinalTotal = float(Conv.replace(',', ''))
            return FinalTotal
        else:
            self.driver.find_element(By.XPATH, "//input[@id='coupon_code']").send_keys(coupon_code)
            self.driver.find_element(By.XPATH, "//button[normalize-space()='Apply coupon']").click()
            value = self.wait.until(
                EC.presence_of_element_located((By.XPATH, "//div[@class='woocommerce-notices-wrapper']//li[1]")))
            assert value.is_displayed() == True
            finalitemvalue = self.driver.find_element(By.XPATH, "//tr[@class='order-total']//bdi[1]")
            Conv = finalitemvalue.text.replace('\u20B9', '')
            FinalTotal = float(Conv.replace(',', ''))
            return FinalTotal

    def continueshoping(self):
        continue_shopping_XPath = "//a[normalize-space()='Continue shopping']"
        self.wait.until(EC.element_to_be_clickable((By.XPATH, continue_shopping_XPath))).click()
        self.log.info("Continue Shopping")

    def getproductssubtotal(self):
        each_product_subtotal_XPath = "//tbody/tr/td[6]"
        self.log.info("Getting Each Product Subtotal - Started")
        NumberOfItem = self.driver.find_elements(By.XPATH, each_product_subtotal_XPath)
        SubTotalList = []
        self.log.info("Number of Products are" + str(len(NumberOfItem)))
        for i in range(1, len(NumberOfItem) + 1):
            locator = "//tbody/" + "tr" + str([i]) + "/td[6]"
            SubTotalList.append(self.driver.find_element(By.XPATH, locator).text)
        self.log.info("Getting Each Product Subtotal - Completed")
        return SubTotalList
