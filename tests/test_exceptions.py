import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from page_objects.exceptions_page import ExceptionsPage


class TestExceptions:
    @pytest.mark.exceptions

    def test_exceptions(self, driver):
        exceptions_page = ExceptionsPage(driver)
        exceptions_page.open()
        exceptions_page.add_second_row()
        assert exceptions_page._is_row2_displayed(), "Row 2 input should be displayed, but it is not"


    @pytest.mark.exceptions

    def test_element_not_interactable(self, driver):
        exceptions_page = ExceptionsPage(driver)
        exceptions_page.open()
        exceptions_page.add_second_row()
        exceptions_page._add_second_food("Sushi")
        assert exceptions_page._get_confirmation_message() == "Row 2 was saved", "Confirmation message is not as expected"



    @pytest.mark.exceptions
    @pytest.mark.invalid_element
    def test_invalid_element_state_exception(self, driver):
        exceptions_page = ExceptionsPage(driver)
        exceptions_page.open()
        exceptions_page._modify_row1_input("Sushi")
        assert exceptions_page._get_confirmation_message() == "Row 1 was saved", "Confirmation message is not as expected"

    @pytest.mark.exceptions
    @pytest.mark.state_element
    @pytest.mark.debug
    def test_state_element_reference(self, driver):
        exceptions_page = ExceptionsPage(driver)
        exceptions_page.open()
        exceptions_page.add_second_row()
        assert not exceptions_page._our_instructions_displayed(), "Instructions text element should not be displayed"

    @pytest.mark.exceptions
    @pytest.mark.timeout_exception
    def test_state_timeout_exception(self, driver):
        exceptions_page = ExceptionsPage(driver)
        exceptions_page.open()
        exceptions_page.add_second_row()
        exceptions_page._is_row2_displayed(), "Row 2 element should be displayed, but it is not"


