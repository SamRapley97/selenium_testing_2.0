import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC


class TestNegativeScenarios:

    @pytest.mark.login
    @pytest.mark.negative
    @pytest.mark.parametrize("username, password, expected_error_message", [("incorrectUser", "Password123", "Your username is invalid!")])
    def test_negative_username(self, driver, username, password, expected_error_message):
        # Open page
        driver.get("https://practicetestautomation.com/practice-test-login/")

        # Type username incorrectUser into Username field
        username_field = driver.find_element(By.ID, "username")
        username_field.send_keys(username)

        # Type password Password123 into Password field
        password_field = driver.find_element(By.ID, "password")
        password_field.send_keys(password)

        # Push submit button
        driver.find_element(By.ID, "submit").click()

        # Verify error message is displayed

        WebDriverWait(driver, timeout=10).until(
            EC.visibility_of_element_located((By.ID, "error"))
        )

        # Verify error message text is Your username is invalid!
        assert expected_error_message in driver.page_source
