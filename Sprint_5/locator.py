from selenium.webdriver.common.by import By
class Locators:
    #страница регистрации
    ELEMENT_NAME_REGISTRATION = By.NAME, "name" #поле "Имя" на странице регистрации
    ELEMENT_EMAIL_REGISTRATION = By.XPATH,  '//label[ text()="Email" ]/parent::div/input' #поле Email на странице регистрации
    ELEMENT_PASSWORD_REGISTRATION = By.XPATH,   '//label[ text()="Пароль" ]/parent::div/input' #поле "Пароль" на странице регистрации
    ELEMENT_BUTTON_REGISTRATION = By.CSS_SELECTOR, 'button.button_button__33qZ0.button_button_type_primary__1O7Bx.button_button_size_medium__3zxIa' #кнопка "Зарегистрироваться" на странице регистрации
    INVALID_PASSWORD_REGISTRATION = By.XPATH, "//p[contains(@class, 'input__error') and text()='Некорректный пароль']" #некорректный пароль на странице регистрации
    # страница входа
    ELEMENT_EMAIL_LOGIN = By.XPATH, '//div[@class="input pr-6 pl-6 input_type_text input_size_default"]/input' #поле Email на странице входа
    ELEMENT_EMAIL_PASSWORD = By.XPATH, '//div[@class="input pr-6 pl-6 input_type_password input_size_default"]/input[@type="password"]' #поле "Пароль" на странице входа
    ELEMENT_BUTTON_LOGIN = By.CSS_SELECTOR, 'button.button_button__33qZ0.button_button_type_primary__1O7Bx.button_button_size_medium__3zxIa' #кнопка "Вход" на странице входа
    #кнопки для перехода на страницу входа
    ELEMENT_BUTTON_LOGIN_LOG_IN_TO_ACCOUNT = By.XPATH, '//button[text()="Войти в аккаунт"]' #кнопка "Войти в аккаунт"
    ELEMENT_BUTTON_LOGIN_PERSONAL_ACCOUNT = By.XPATH, '//p[text()="Личный Кабинет"]' #кнопка "Личный кабинет"
    ELEMENT_BUTTON_LOGIN_REGISTRATION_FORM = By.XPATH, '//a[text()="Войти"]' #кнопка "Войти" на странице формы регистрации
    ELEMENT_BUTTON_LOGIN_PASSWORD_RESTORATION_FORM = By.XPATH, '//a[text()="Войти"]' #кнопка входа на странице формы восстановления пароля
    #кнопка "Личный кабинет", пользователь авторизован
    ELEMENT_BUTTON_LOGIN_PERSONAL_ACCOUNT_USER_AUTHORIZED = By.XPATH, "//p[@class='AppHeader_header__linkText__3q_va ml-2' and text()='Личный Кабинет']"
    #кнопка "Конструктор", пользователь авторизован
    ELEMENT_BUTTON_CONSTRUCTOR_ACCOUNT_USER_AUTHORIZED = By.XPATH, "//a[contains(@class, 'AppHeader_header__link__3D_hX') and .//p[text()='Конструктор']]"
    #кнопка "Выход"
    ELEMENT_BUTTON_EXIT = By.XPATH, "//button[text()='Выход']"
    #разделы булки, соусы, начинки
    ELEMENT_BUNS = By.XPATH, "//span[contains(text(),'Булки')]" # раздел "Булки"
    ELEMENT_SAUCE = By.XPATH, "//span[contains(text(),'Соусы')]" # раздел "Соусы"
    ELEMENT_FILLING = By.XPATH, "//span[contains(text(),'Начинки')]" # раздел "Начинки"
    ELEMENT_BUNS_DIV = By.XPATH, "//span[contains(text(),'Булки')]/parent::div" # контейнер раздела "Булки"
    ELEMENT_SAUCE_DIV = By.XPATH, "//span[contains(text(),'Соусы')]/parent::div" # контейнер раздела "Соусы"
    ELEMENT_FILLING_DIV = By.XPATH, "//span[contains(text(),'Начинки')]/parent::div" # контейнер раздела "Начинки"
