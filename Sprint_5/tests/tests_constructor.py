from locator import Locators
class TestConstructor:
    def test_constructor_sauce(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(*Locators.ELEMENT_SAUCE).click()
        assert "tab_tab_type_current__2BEPc" in driver.find_element(*Locators.ELEMENT_SAUCE_DIV).get_attribute("class")

    def test_constructor_buns(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(*Locators.ELEMENT_SAUCE).click()
        driver.find_element(*Locators.ELEMENT_BUNS).click()
        assert "tab_tab_type_current__2BEPc" in driver.find_element(*Locators.ELEMENT_BUNS_DIV).get_attribute("class")

    def test_constructor_filling(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(*Locators.ELEMENT_FILLING).click()
        assert "tab_tab_type_current__2BEPc" in driver.find_element(*Locators.ELEMENT_FILLING_DIV).get_attribute("class")
