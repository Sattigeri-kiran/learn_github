import logging
from selenium.webdriver.common.by import By
from utilities.utils import Utils


class TestContactUs:
    log = Utils.custlogger(logLevel=logging.DEBUG)

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    def test_contact_us(self):
        name_field_XPath = self.driver.find_element(By.XPATH, "//input[@id='name']")
        name_field_XPath.send_keys("Test Case")
        self.log.debug("Entered Name")
        email_field_XPath = self.driver.find_element(By.XPATH, "//input[@id='email']")
        email_field_XPath.send_keys("TestCase@gmail.com")
        self.log.debug("Entered EmailId")
        message_field_XPath = self.driver.find_element(By.XPATH, "//textarea[@id='message']")
        message_field_XPath.send_keys("Test Message")
        self.log.debug("Entered Message")

    def test_email(self, email_Id):
        email_field_XPath = self.driver.find_element(By.XPATH, "//input[@id='email']")
        email_field_XPath.send_keys(email_Id)
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Submit']").click()
        popup_text = email_field_XPath.get_attribute("validationMessage")
        self.log.info("Popup message is verified for" + email_Id)
        return popup_text
