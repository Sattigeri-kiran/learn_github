import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class TestItemCart:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    def AddItemQty(self, productname, productqty):
        CartProducts = self.driver.find_elements(By.XPATH, "//td[@class='product-quantity']//div//input")
        for i in CartProducts:
            product = self.driver.find_elements(By.XPATH, "//td[@class='product-name']//a")
            if product[0].text == productname:
                i.clear()
                i.send_keys(productqty)
            else:
                i.clear()
                i.send_keys(productqty)
            time.sleep(5)
        element = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Update basket']")))
        element.click()

    def getItemcost(self):
        Subtotal = self.wait.until(EC.presence_of_element_located((By.XPATH, "//tr[@class='cart-subtotal']//bdi[1]")))
        Subtotal_new = self.driver.find_element(By.XPATH, "//tr[@class='cart-subtotal']//bdi[1]")
        Conv1 = Subtotal.text.replace('\u20B9', '')
        Subtotal_new1 = float(Conv1.replace(',', ''))
        return Subtotal_new1

    def getTotalcost(self):
        totalitemsvalue = self.wait.until(EC.presence_of_element_located((By.XPATH, "//tr[@class='order-total']//bdi[1]")))
        Conversion = totalitemsvalue.text.replace('\u20B9', '')
        Total = float(Conversion.replace(',', ''))
        return Total

    def testapplycoupon(self, couponcode, total):
        if total >= 999.00:
            time.sleep(4)
            self.driver.find_element(By.XPATH, "//input[@id='coupon_code']").send_keys(couponcode)
            time.sleep(3)
            self.driver.find_element(By.XPATH, "//button[normalize-space()='Apply coupon']").click()
            time.sleep(3)
            finalitemvalue = self.driver.find_element(By.XPATH, "//tr[@class='order-total']//bdi[1]")
            Conv = finalitemvalue.text.replace('\u20B9', '')
            FinalTotal = float(Conv.replace(',', ''))
            return FinalTotal
        else:
            self.driver.find_element(By.XPATH, "//input[@id='coupon_code']").send_keys(couponcode)
            self.driver.find_element(By.XPATH, "//button[normalize-space()='Apply coupon']").click()
            value = self.wait.until(
                EC.presence_of_element_located((By.XPATH, "//div[@class='woocommerce-notices-wrapper']//li[1]")))
            assert value.is_displayed() == True
            finalitemvalue = self.driver.find_element(By.XPATH, "//tr[@class='order-total']//bdi[1]")
            Conv = finalitemvalue.text.replace('\u20B9', '')
            FinalTotal = float(Conv.replace(',', ''))
            return FinalTotal

    def continueshoping(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Continue shopping']"))).click()

    def getproductssubtotal(self):
        NumberOfItem = self.driver.find_elements(By.XPATH, "//tbody/tr/td[6]")
        SubTotalList = []
        print(len(NumberOfItem))
        for i in range(1, len(NumberOfItem) + 1):
            locator = "//tbody/" + "tr" + str([i]) + "/td[6]"
            SubTotalList.append(self.driver.find_element(By.XPATH, locator).text)
        return SubTotalList
