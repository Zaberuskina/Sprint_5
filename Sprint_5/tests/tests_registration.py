#Успешная регистрация
from locator import Locators
from helpers import generate_random_email, generate_random_password
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class TestsRegistration:

    def test_registration_successful(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/register")

        # Ввод данных для регистрации
        driver.find_element(*Locators.ELEMENT_NAME_REGISTRATION).send_keys("Анна")
        driver.find_element(*Locators.ELEMENT_EMAIL_REGISTRATION).send_keys(generate_random_email())
        driver.find_element(*Locators.ELEMENT_PASSWORD_REGISTRATION).send_keys(generate_random_password())

        # Нажатие на кнопку для регистрации
        driver.find_element(*Locators.ELEMENT_BUTTON_REGISTRATION).click()

        # Ожидание перенаправления на страницу логина 10 сек
        WebDriverWait(driver, 10).until(EC.url_to_be("https://stellarburgers.nomoreparties.site/login"))

        # Проверка, что происходит переход на страницу входа
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/login"

#Некорректный пароль
    def test_invalid_password(self, driver):
        # Ввод некорректного пароля
        driver.get("https://stellarburgers.nomoreparties.site/register")
        driver.find_element(*Locators.ELEMENT_PASSWORD_REGISTRATION).send_keys("1203")
        driver.find_element(*Locators.ELEMENT_EMAIL_REGISTRATION).click()
        #Проверка об ошибке
        invalid_password = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(Locators.INVALID_PASSWORD_REGISTRATION))
        assert invalid_password.text == "Некорректный пароль"
