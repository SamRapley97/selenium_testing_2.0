import time
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# Go to webpage
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
time.sleep(5)
driver.get("https://practicetestautomation.com/practice-test-login/")

# Type username student into Username field
username_locator = driver.find_element(By.ID, "username")
username_locator.send_keys("student")

# Type password Password123 into Password field
password_locator = driver.find_element(By.ID, "password")
password_locator.send_keys("Password123")

# Push Submit button
button_locator = driver.find_element(By.XPATH, "//button[@id='submit']")
button_locator.click()

# Verify new page URL contains practicetestautomation.com/logged-in-successfully/
assert driver.current_url == "https://practicetestautomation.com/logged-in-successfully/", f"{driver.current_url} does not match expected"

# Verify new page contains expected text ('Congratulations' or 'successfully logged in')
assert 'Congratulation' or 'successfully logged in' in driver.page_source, "Neither of the two phrases were found in the page source"

# Verify button Log out is displayed on the new page


def check_logout_button_exists():
    try:
        driver.find_element(By.CSS_SELECTOR, ".has-background.has-text-color.has-very-dark-gray-background-color")
    except NoSuchElementException:
        print("No logout button has been found")
        return False
    return True


check_logout_button_exists()

driver.quit()