from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from base.base_driver import BaseDriver
from pages.aboutuspage import TestContactUs
from pages.produtpage import TestProductPage
from pages.reviewpage import TestReviewPage
import logging
from utilities.utils import Utils


class TestGSHomePage(BaseDriver):
    log = Utils.custlogger(logLevel=logging.INFO)

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    def test_shopitems(self, shop_item):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, shop_item))).click()
        self.log.info("Clicked on Item")
        product_page = TestProductPage(self.driver, self.wait)
        self.log.info("In Product Page")
        return product_page

    def test_switchtoproduct(self, item):
        switchproduct = self.driver.find_element(By.XPATH, '//*[@id="menu-item-968"]/a')
        action = ActionChains(self.driver)
        action.move_to_element(switchproduct).perform()
        self.wait.until(EC.element_to_be_clickable((By.XPATH, item))).click()
        self.log.info("Switched to " + item + "Sweet")

    def test_review_page(self):
        self.driver.find_element(By.ID, 'menu-item-1643').click()
        self.log.info("Clicked on Item")
        review_page = TestReviewPage(self.driver, self.wait)
        self.log.info("In Review Page")
        return review_page

    def test_contactuspage(self):
        self.driver.find_element(By.ID, "menu-item-1599").click()
        self.log.info("Clicked on Contact Us Page")
        contactus_page = TestContactUs(self.driver, self.wait)
        self.log.info("In Contact Us Page")
        return contactus_page
