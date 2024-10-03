from locator import Locators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class TestTransitionPersonalAccount:
    def test_transition_personal_account(self, driver, authorization):
        driver.find_element(*Locators.ELEMENT_BUTTON_LOGIN_PERSONAL_ACCOUNT_USER_AUTHORIZED).click()
        # Ожидание перенаправления на страницу профиля
        WebDriverWait(driver, 20).until(EC.url_to_be("https://stellarburgers.nomoreparties.site/account/profile"))
        # Проверка, что происходит переход на страницу личного кабинета
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/account/profile"


