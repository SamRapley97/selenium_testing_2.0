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

    @pytest.mark.exceptions
    @pytest.mark.debug
    def test_element_not_interactable(self, driver):
        # Open the page
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")

        # Click add button
        driver.find_element(By.ID, "add_btn").click()

        # Wait for row2 to become visible
        WebDriverWait(driver, timeout=15).until(
            EC.visibility_of_element_located((By.XPATH,
                                              "//div[@id='row2']/input[@class='input-field']")))

        # Type input into row 2
        row2 = driver.find_element(By.XPATH, "//div[@id='row2']/input[@class='input-field']")
        row2.send_keys("Curry")

        # Push save button
        save = driver.find_element(By.XPATH, "//div[@id='row2']/button[@name='Save']")
        save.click()

        # Verify text is saved
        confirmation_element = driver.find_element(By.ID, "confirmation")
        confirmation_message = confirmation_element.text
        assert confirmation_message == "Row 2 was saved", "Confirmation message is not as expected"

    @pytest.mark.exceptions
    @pytest.mark.invalid_element
    def test_invalid_element_state_exception(self, driver):
        # Open the page
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")

        # Clear input field
        row1_button = driver.find_element(By.ID, "edit_btn")
        row1_button.click()

        row1 = driver.find_element(By.XPATH, "//div[@id='row1']/input[@class='input-field']")
        wait = WebDriverWait(driver, 10)
        wait.until(EC.element_to_be_clickable(row1))
        row1.clear()

        # Type text into the input field
        row1.send_keys("Hello darkness my old friend")

        # Verify text changed
        text = row1.get_attribute("value")
        assert text == "Hello darkness my old friend", f"${text} does not equal 'Hello darkness my old friend'"



