from locator import Locators

class TestsLogin:
    # вход по кнопке «Войти в аккаунт» на главной
    def test_login_to_account(self, driver_login):
        driver_login.get("https://stellarburgers.nomoreparties.site/")
        driver_login.find_element(*Locators.ELEMENT_BUTTON_LOGIN_LOG_IN_TO_ACCOUNT).click()

    #вход через кнопку «Личный кабинет»
    def test_login_personal_account(self, driver_login):
        driver_login.get("https://stellarburgers.nomoreparties.site/")
        driver_login.find_element(*Locators.ELEMENT_BUTTON_LOGIN_PERSONAL_ACCOUNT).click()

    #вход через кнопку в форме регистрации
    def test_login_registration_form(self, driver_login):
        driver_login.get("https://stellarburgers.nomoreparties.site/register")
        driver_login.find_element(*Locators.ELEMENT_BUTTON_LOGIN_REGISTRATION_FORM).click()

    #вход через кнопку в форме восстановления пароля
    def test_login_password_recovery_form(self, driver_login):
        driver_login.get("https://stellarburgers.nomoreparties.site/forgot-password")
        driver_login.find_element(*Locators.ELEMENT_BUTTON_LOGIN_PASSWORD_RESTORATION_FORM).click()


