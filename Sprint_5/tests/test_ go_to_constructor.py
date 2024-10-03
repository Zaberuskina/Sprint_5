from locator import Locators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class TestGoToConstructor:
    def test_go_to_constructor(self, driver, authorization):
        driver.find_element(*Locators.ELEMENT_BUTTON_LOGIN_PERSONAL_ACCOUNT_USER_AUTHORIZED).click()
        driver.find_element(*Locators.ELEMENT_BUTTON_CONSTRUCTOR_ACCOUNT_USER_AUTHORIZED).click()
        WebDriverWait(driver, 15).until(EC.url_to_be("https://stellarburgers.nomoreparties.site/"))
        # Проверка, что происходит переход на страницу конструктора
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/"