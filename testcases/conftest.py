import os
import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="class")
def GSSetup(request):
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    driver.get("https://gokaksweets.com")
    wait = WebDriverWait(driver, 10)
    driver.maximize_window()
    request.cls.driver = driver
    request.cls.wait = wait
    yield
    driver.quit()

def pytest_html_report_title(report):
    report.title = "Gokak Sweets Test"
