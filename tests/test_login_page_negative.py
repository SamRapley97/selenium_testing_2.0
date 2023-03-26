import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC


class TestNegativeScenarios:

    @pytest.mark.login
    @pytest.mark.negative
    def test_negative_username(self, driver):
        # Open page
        driver.get("https://practicetestautomation.com/practice-test-login/")

        # Type username incorrectUser into Username field
        username_field = driver.find_element(By.ID, "username")
        username_field.send_keys("incorrectUser")

        # Type password Password123 into Password field
        password_field = driver.find_element(By.ID, "password")
        password_field.send_keys("Password123")

        # Push submit button
        driver.find_element(By.ID, "submit").click()

        # Verify error message is displayed

        WebDriverWait(driver, timeout=10).until(
            EC.visibility_of_element_located((By.ID, "error"))
        )

        # Verify error message text is Your username is invalid!
        assert "Your username is invalid!" in driver.page_source
