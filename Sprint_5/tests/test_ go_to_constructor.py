from locator import Locators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class TestGoToConstructor:
    def test_go_to_constructor(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(*Locators.ELEMENT_BUTTON_LOGIN_LOG_IN_TO_ACCOUNT).click()
        driver.find_element(*Locators.ELEMENT_EMAIL_LOGIN).send_keys(
            "0087687@ya.ru")
        driver.find_element(*Locators.ELEMENT_EMAIL_PASSWORD).send_keys(
            "1203@ya.ru")
        # Нажатие на кнопку для входа
        driver.find_element(*Locators.ELEMENT_BUTTON_LOGIN).click()
        WebDriverWait(driver, 10).until(EC.url_to_be("https://stellarburgers.nomoreparties.site/"))
        driver.find_element(*Locators.ELEMENT_BUTTON_LOGIN_PERSONAL_ACCOUNT_USER_AUTHORIZED).click()
        driver.find_element(*Locators.ELEMENT_BUTTON_CONSTRUCTOR_ACCOUNT_USER_AUTHORIZED).click()
        WebDriverWait(driver, 15).until(EC.url_to_be("https://stellarburgers.nomoreparties.site/"))
        # Проверка, что происходит переход на страницу конструктора
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/"
        print("Успешный переход на страницу Конструктора")