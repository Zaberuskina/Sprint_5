from locator import Locators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class TestsLogin:
    # вход по кнопке «Войти в аккаунт» на главной
    def test_login_to_account(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(*Locators.ELEMENT_BUTTON_LOGIN_LOG_IN_TO_ACCOUNT).click()
        driver.find_element(*Locators.ELEMENT_EMAIL_LOGIN).send_keys(
            "0087687@ya.ru")
        driver.find_element(*Locators.ELEMENT_EMAIL_PASSWORD).send_keys(
            "1203@ya.ru")
        # Нажатие на кнопку для входа
        driver.find_element(*Locators.ELEMENT_BUTTON_LOGIN).click()
        # Ожидание перехода на главную страницу
        WebDriverWait(driver, 10).until(EC.url_to_be("https://stellarburgers.nomoreparties.site/"))
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/"

    #вход через кнопку «Личный кабинет»
    def test_login_personal_account(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(*Locators.ELEMENT_BUTTON_LOGIN_PERSONAL_ACCOUNT).click()
        driver.find_element(*Locators.ELEMENT_EMAIL_LOGIN).send_keys(
            "0087687@ya.ru")
        driver.find_element(*Locators.ELEMENT_EMAIL_PASSWORD).send_keys(
            "1203@ya.ru")
        # Нажатие на кнопку для входа
        driver.find_element(*Locators.ELEMENT_BUTTON_LOGIN).click()
        # Ожидание перехода на главную страницу
        WebDriverWait(driver, 10).until(EC.url_to_be("https://stellarburgers.nomoreparties.site/"))
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/"


    #вход через кнопку в форме регистрации
    def test_login_registration_form(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/register")
        driver.find_element(*Locators.ELEMENT_BUTTON_LOGIN_REGISTRATION_FORM).click()
        driver.find_element(*Locators.ELEMENT_EMAIL_LOGIN).send_keys(
            "0087687@ya.ru")
        driver.find_element(*Locators.ELEMENT_EMAIL_PASSWORD).send_keys(
            "1203@ya.ru")
        # Нажатие на кнопку для входа
        driver.find_element(*Locators.ELEMENT_BUTTON_LOGIN).click()
        # Ожидание перехода на главную страницу
        WebDriverWait(driver, 10).until(EC.url_to_be("https://stellarburgers.nomoreparties.site/"))
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/"


    #вход через кнопку в форме восстановления пароля
    def test_login_password_recovery_form(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/forgot-password")
        driver.find_element(*Locators.ELEMENT_BUTTON_LOGIN_PASSWORD_RESTORATION_FORM).click()
        driver.find_element(*Locators.ELEMENT_EMAIL_LOGIN).send_keys(
            "0087687@ya.ru")
        driver.find_element(*Locators.ELEMENT_EMAIL_PASSWORD).send_keys(
            "1203@ya.ru")
        # Нажатие на кнопку для входа
        driver.find_element(*Locators.ELEMENT_BUTTON_LOGIN).click()
        # Ожидание перехода на главную страницу
        WebDriverWait(driver, 10).until(EC.url_to_be("https://stellarburgers.nomoreparties.site/"))
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/"


