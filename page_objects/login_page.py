from selenium.webdriver.common import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.wait import expected_conditions as EC

from page_objects.BasePage import BasePage


class LoginPage(BasePage):
    __url = "https://practicetestautomation.com/practice-test-login/"
    __username_field = (By.ID, "username")
    __password_locator = (By.ID, "password")
    __button_locator = (By.XPATH, "//button[@id='submit']")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open(self):
        super().open_url(self.__url)

    def execute_login(self, username: str, password: str):
        super().type(self.__username_field, username)
        super().type(self.__password_locator, password)
        super().click(self.__button_locator)


