from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from page_objects.BasePage import BasePage


class LoggedInSuccessfullyPage(BasePage):
    _url = "https://practicetestautomation.com/practice-test-login/"
    __header_locator = (By.TAG_NAME, "h1")
    __log_out_button_locator = (By.LINK_TEXT, "Log out")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    @property
    def get_current_url(self) -> str:
        return self._driver.current_url

    @property
    def get_expected_url(self) -> str:
        return  self._url

    @property
    def header(self) -> str:
        return super().get_text(self.__header_locator)

    def is_logout_button_displayed(self) -> bool:
        return super.is_displayed(self.__log_out_button_locator)
