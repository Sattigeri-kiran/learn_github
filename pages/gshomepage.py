from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.produtpage import TestProductPage
from pages.reviewpage import TestReviewPage


class TestGSHomePage:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    def test_shopitems(self, shopitem):
        self.driver.find_element(By.XPATH, shopitem).click()
        product_page = TestProductPage(self.driver, self.wait)
        return product_page

    def test_switchtoproduct(self, item):
        switchproduct = self.driver.find_element(By.XPATH, '//*[@id="menu-item-968"]/a')
        action = ActionChains(self.driver)
        action.move_to_element(switchproduct).perform()
        self.wait.until(EC.element_to_be_clickable((By.XPATH, item))).click()

    def test_review_page(self):
        self.driver.find_element(By.ID, 'menu-item-1643').click()
        review_page = TestReviewPage(self.driver, self.wait)
        return review_page

