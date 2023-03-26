import pytest
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService


@pytest.fixture()
def driver():
    print("Create chrome driver")
    my_driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    yield my_driver
    print("Closing chrome driver")
    my_driver.quit()
