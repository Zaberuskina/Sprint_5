from locator import Locators
import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture()
def driver_login():
    driver = webdriver.Chrome()
    yield driver
    driver.find_element(*Locators.ELEMENT_EMAIL_LOGIN).send_keys(
        "0087687@ya.ru")
    driver.find_element(*Locators.ELEMENT_EMAIL_PASSWORD).send_keys(
        "1203@ya.ru")
    # Нажатие на кнопку для входа
    driver.find_element(*Locators.ELEMENT_BUTTON_LOGIN).click()
    # Ожидание перехода на главную страницу
    WebDriverWait(driver, 10).until(EC.url_to_be("https://stellarburgers.nomoreparties.site/"))
    print("Переход на страницу успешен.")
    driver.quit()




