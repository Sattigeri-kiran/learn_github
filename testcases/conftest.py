import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from ftplib import FTP


@pytest.fixture(scope="class")
def GSSetup(request, browser, url):
    if browser == "chrome":
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    elif browser == "firefox":
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    elif browser == "edge":
        driver = webdriver.Edge(EdgeChromiumDriverManager().install)
    driver.get(url)  # https://gokaksweets.com/
    wait = WebDriverWait(driver, 10)
    driver.maximize_window()
    request.cls.driver = driver
    request.cls.wait = wait
    yield
    driver.quit()

@pytest.fixture(scope="class")
def FTPsetup(request):
    ftp = FTP("ftp.dlptest.com")
    ftp.login("dlpuser", 'rNrKYTX9g7z3RgJRmxWuGHbeu')
    print(ftp.getwelcome())
    request.cls.ftp = ftp
    yield
    ftp.close()


def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--url")


@pytest.fixture(scope="class", autouse=True)
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope="class", autouse=True)
def url(request):
    return request.config.getoption("--url")


def pytest_html_report_title(report):
    report.title = "Gokak Sweets Test Report"
