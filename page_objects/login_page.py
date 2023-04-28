from selenium.webdriver.common import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.wait import expected_conditions as EC


class LoginPage:
    __url = "https://practicetestautomation.com/practice-test-login/"
    __username_field = (By.ID, "username")
    __password_locator = (By.ID, "password")
    __button_locator = (By.XPATH, "//button[@id='submit']")

    def __init__(self, driver: WebDriver):
        self._driver = driver

    def open(self):
        self._driver.get(self.__url)

    def execute_login(self, username: str, password: str):
        wait = WebDriverWait(self._driver, 10)

        wait.until(EC.visiblity_of_element_located(self.__username_field))
        self._driver.find_element(self.__username_field).send_keys(username)

        wait.until(EC.visiblity_of_element_located(self.__password_locator))
        self._driver.find_element(self.__password_locator).send_keys(password)

        wait.until(EC.visiblity_of_element_located(self.__button_locator))
        self._driver.find_element(self.__button_locator).click()

