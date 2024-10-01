from locator import Locators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class TestLogout:
    def test_logout(self, driver):
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
        # Ожидание перенаправления на страницу профиля
        WebDriverWait(driver, 10).until(EC.url_to_be("https://stellarburgers.nomoreparties.site/account/profile"))
        # Ожидание перенаправления на страницу профиля
        WebDriverWait(driver, 10).until(EC.url_to_be("https://stellarburgers.nomoreparties.site/account/profile"))
        driver.find_element(*Locators.ELEMENT_BUTTON_EXIT).click()
        WebDriverWait(driver, 10).until(EC.url_to_be("https://stellarburgers.nomoreparties.site/login"))
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/login"
        print("Успешный разлогин")