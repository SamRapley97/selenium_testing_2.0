import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestExceptions:
    @pytest.mark.exceptions
    def test_exceptions(self, driver):
        # Open the page
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")

        # Click add button
        driver.find_element(By.ID, "add_btn").click()

        # Wait for row2 to become visible
        WebDriverWait(driver, timeout=15).until(
            EC.visibility_of_element_located((By.XPATH,
                                              "//div[@id='row2']/input[@class='input-field']")))

        # Verify Row 2 input field is displayed

        input_field = driver.find_element(By.XPATH, "//div[@id='row2']/input[@class='input-field']")
        assert input_field.is_displayed()



