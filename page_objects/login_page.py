from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from page_objects.base_page import BasePage
from selenium.webdriver.support.wait import WebDriverWait


class LoginPage(BasePage):
    __url = "https://practicetestautomation.com/practice-test-login/"
    __username_field = (By.ID, "username")
    __password_locator = (By.ID, "password")
    __button_locator = (By.XPATH, "//button[@id='submit']")
    __error_message = (By.ID, "error")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open(self):
        super()._open_url(self.__url)

    def execute_login(self, username: str, password: str):
        super()._type(self.__username_field, username)
        super()._type(self.__password_locator, password)
        super()._click(self.__button_locator)

    def get_error_message(self) -> str:
        return super().get_text(self.__error_message, time=3)
