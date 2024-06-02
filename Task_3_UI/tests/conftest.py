import os
import pytest

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

HEADLESS = False
BASE_PAGE = 'http://localhost:5000'


@pytest.fixture()
def browser():
    options = ChromeOptions()
    if HEADLESS:
        options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-gpu")
    options.add_argument("disable-infobars")

    driver = webdriver.Chrome(options=options)

    driver.maximize_window()
    driver.implicitly_wait(5)
    driver.get(BASE_PAGE)

    yield driver

    driver.quit()
