from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from page_objects.base_page import BasePage


class ExceptionsPage(BasePage):
    __url = "https://practicetestautomation.com/practice-test-exceptions/"
    __add_button_locator = (By.ID, "add_btn")
    __row1_input_field = (By.XPATH, "//div[@id='row1']/input")
    __input_field = (By.XPATH, "//div[@id='row2']/input")
    __row1_edit_button = (By.ID, "edit_btn")
    __row_1_save_button = (By.XPATH, "//div[@id='row1']/button[@name='Save']")
    __row2_save_button = (By.XPATH, "//div[@id='row2']/button[@name='Save']")
    __confirmation_element = (By.ID, "confirmation")
    __instructions = (By.ID, "instructions")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open(self):
        super()._open_url(self.__url)

    def add_second_row(self):
        super()._click(self.__add_button_locator)
        super()._wait_until_element_visible(self.__input_field)

    def _is_row2_displayed(self) -> bool:
        return super()._is_displayed(self.__input_field)

    def _add_second_food(self, food: str):
        super()._type(self.__input_field, food)
        super()._click(self.__row2_save_button)
        super()._wait_until_element_visible(self.__confirmation_element)

    def _get_confirmation_message(self) -> str:
        return super().get_text(self.__confirmation_element, time=3)

    def _modify_row1_input(self, food: str):
        super()._click(self.__row1_edit_button)
        super()._wait_until_element_clickable(self.__row1_input_field)
        super()._clear(self.__row1_input_field)
        super()._type(self.__row1_input_field, food)
        super()._click(self.__row_1_save_button)
        super()._wait_until_element_visible(self.__confirmation_element)

    def _our_instructions_displayed(self):
        super()._is_displayed(self.__instructions)