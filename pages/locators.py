from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_SUBMIT = (By.CSS_SELECTOR, "button[value='Log In']")
    REGISTRATION_SUBMIT = (By.CSS_SELECTOR, "button[value='Register']")