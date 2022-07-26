import time
import logging
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from utilities.utils import Utils


class TestReviewPage:
    log = Utils.custlogger(logLevel=logging.WARNING)

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    def test_sort(self, sortby, sort_id):
        #sort_id = 'wc-block-components-sort-select__select-0'
        self.wait.until(EC.element_to_be_clickable((By.ID, sort_id)))
        dropdown = self.driver.find_element(By.ID, sort_id)
        dd = Select(dropdown)
        dd.select_by_index(sortby)
        self.log.warning("Sorted the Reviews")
        time.sleep(5)

    def backtotop(self):
        backtotop = self.driver.find_element(By.XPATH, "//span[contains(text(),'Back to top')]")
        self.driver.execute_script("arguments[0].scrollIntoView();", backtotop)
        backtotop.click()
        self.log.warning("Moved to Top of page")

    def loadmorereviews(self):
        current_reviews = self.driver.find_elements(By.XPATH,
                                                    "//div[@class='main-content clear-fix boxed-wrapper']//li")
        loadmore = self.driver.find_element(By.XPATH, "//button[@class='wp-block-button__link']")
        while bool(loadmore):
            try:
                loadmore.click()
                loadmore = self.driver.find_element(By.XPATH, "//button[@class='wp-block-button__link']")
                self.driver.execute_script("arguments[0].scrollIntoView();", loadmore)
            except (NoSuchElementException, StaleElementReferenceException):
                loadmore = False
        self.log.warning("Loaded all reviews ")
        load_reviews = self.driver.find_elements(By.XPATH,
                                                 "//div[@class='main-content clear-fix boxed-wrapper']//li")
        list1 = [len(load_reviews), len(current_reviews)]
        return list1

    def review_checkbox(self):
        review_checkbox = self.driver.find_element(By.ID, "wp-comment-cookies-consent")
        review_checkbox.click()
        self.driver.execute_script("arguments[0].scrollIntoView();", review_checkbox)
        self.driver.implicitly_wait(10)
        checkbox = self.driver.find_element(By.ID, "wp-comment-cookies-consent").is_selected()
        return checkbox
