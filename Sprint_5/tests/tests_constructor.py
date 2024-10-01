from locator import Locators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class TestConstructor:
    def test_constructor_rolls1(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(*Locators.ELEMENT_BUTTON_LOGIN_LOG_IN_TO_ACCOUNT).click()
        driver.find_element(*Locators.ELEMENT_EMAIL_LOGIN).send_keys(
            "0087687@ya.ru")
        driver.find_element(*Locators.ELEMENT_EMAIL_PASSWORD).send_keys(
            "1203@ya.ru")
        # Нажатие на кнопку для входа
        driver.find_element(*Locators.ELEMENT_BUTTON_LOGIN).click()
        WebDriverWait(driver, 10).until(EC.url_to_be("https://stellarburgers.nomoreparties.site/"))
        driver.find_element(*Locators.ELEMENT_SAUCE).click()
        assert "tab_tab_type_current__2BEPc" in driver.find_element(*Locators.ELEMENT_SAUCE_DIV).get_attribute("class")

    def test_constructor_rolls2(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(*Locators.ELEMENT_BUTTON_LOGIN_LOG_IN_TO_ACCOUNT).click()
        driver.find_element(*Locators.ELEMENT_EMAIL_LOGIN).send_keys(
            "0087687@ya.ru")
        driver.find_element(*Locators.ELEMENT_EMAIL_PASSWORD).send_keys(
            "1203@ya.ru")
        # Нажатие на кнопку для входа
        driver.find_element(*Locators.ELEMENT_BUTTON_LOGIN).click()
        WebDriverWait(driver, 10).until(EC.url_to_be("https://stellarburgers.nomoreparties.site/"))
        driver.find_element(*Locators.ELEMENT_SAUCE).click()
        driver.find_element(*Locators.ELEMENT_BUNS).click()
        assert "tab_tab_type_current__2BEPc" in driver.find_element(*Locators.ELEMENT_BUNS_DIV).get_attribute("class")

    def test_3(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(*Locators.ELEMENT_BUTTON_LOGIN_LOG_IN_TO_ACCOUNT).click()
        driver.find_element(*Locators.ELEMENT_EMAIL_LOGIN).send_keys(
            "0087687@ya.ru")
        driver.find_element(*Locators.ELEMENT_EMAIL_PASSWORD).send_keys(
            "1203@ya.ru")
        # Нажатие на кнопку для входа
        driver.find_element(*Locators.ELEMENT_BUTTON_LOGIN).click()
        WebDriverWait(driver, 10).until(EC.url_to_be("https://stellarburgers.nomoreparties.site/"))
        driver.find_element(*Locators.ELEMENT_FILLING).click()
        assert "tab_tab_type_current__2BEPc" in driver.find_element(*Locators.ELEMENT_FILLING_DIV).get_attribute("class")
